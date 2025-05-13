const MiniAppExtension = {
  counter: 0,
  environmentUrl: window.Capacitor ? "capacitor://localhost" : (document.referrer || "https://dev-bot.convegenius.ai/"),
  callbackMap: {},
  PERMISSIONS: {
    CAMERA: "CAMERA",
    FILE_PICKER: "FILE_PICKER",
    LOCATION: "LOCATION",
    MICROPHONE: "MICROPHONE",
  },
  getKeyForFunction: (functionName, requestId) => {
    return [functionName, requestId].join("_");
  },
  call: (functionName, args = {}, callback) => {
    MiniAppExtension.counter += 1;
    let requestId = MiniAppExtension.counter;
    args["requestId"] = requestId;
    let key = MiniAppExtension.getKeyForFunction(functionName, requestId);
    if (!MiniAppExtension.callbackMap[key]) {
      MiniAppExtension.callbackMap[key] = [];
    }
    MiniAppExtension.callbackMap[key].push(callback);
    MiniAppExtension.postMessage(functionName, args);
  },
  postMessage: (functionName, args) => {
    let data = { functionName, args };
    console.log("Sdk sending to CG frontend if available", data);
    if ("WebviewChannel" in window) {
      WebviewChannel.postMessage(JSON.stringify(data));
    } else if (window.parent != window) {
      window.parent.postMessage(data, MiniAppExtension.environmentUrl);
    }
  },
  frontendCall: (event) => {
    const { functionName, args } = event;
    const { requestId } = args;
    let key = MiniAppExtension.getKeyForFunction(functionName, requestId);
    if (
      MiniAppExtension.callbackMap[key] &&
      MiniAppExtension.callbackMap[key].length > 0
    ) {
      callback = MiniAppExtension.callbackMap[key].shift();
      callback(args);
    }
  },
  getUserConsent: (callback) => {
    MiniAppExtension.call("getUserConsent", {}, (args) => {
      console.log("Callback of sdk called", args);
      if (callback) callback(args);
    });
  },
  setItem: (key, value, callback) => {
    MiniAppExtension.call("setItem", { key, value }, (args) => {
      console.log("Callback of sdk called", args);
      if (callback) callback(args);
    });
  },
  getItem: (key, callback) => {
    MiniAppExtension.call("getItem", { key }, (args) => {
      console.log("Callback of sdk called", args);
      if (callback) callback(args);
    });
  },
  getAllItems: (callback) => {
    MiniAppExtension.call("getAllItems", {}, (args) => {
      console.log("Callback of sdk called", args);
      if (callback) callback(args);
    });
  },
  removeItem: (key, callback) => {
    MiniAppExtension.call("removeItem", { key }, (args) => {
      console.log("Callback of sdk called", args);
      if (callback) callback(args);
    });
  },
  removeAllItems: (callback) => {
    MiniAppExtension.call("removeAllItems", {}, (args) => {
      console.log("Callback of sdk called", args);
      if (callback) callback(args);
    });
  },
  checkPermission: (permission, callback) => {
    if (!MiniAppExtension.PERMISSIONS[permission]) return;
    MiniAppExtension.call("checkPermission", { permission }, (args) => {
      console.log("Callback of sdk called", args);
      if (callback) callback(args);
    });
  },
  getPermission: (permission, callback) => {
    if (!MiniAppExtension.PERMISSIONS[permission]) return;
    MiniAppExtension.call("getPermission", { permission }, (args) => {
      console.log("Callback of sdk called", args);
      if (callback) callback(args);
    });
  },
  supportedCalls: [
    "getUserConsent",
    "setItem",
    "getItem",
    "getAllItems",
    "removeItem",
    "removeAllItems",
    "checkPermission",
    "getPermission",
  ],
};
window.addEventListener(
  "message",
  (event) => {
    const { functionName, args } = event.data;
    if (!functionName || !args) return;
    const { requestId } = args;
    let key = MiniAppExtension.getKeyForFunction(functionName, requestId);
    if (
      MiniAppExtension.supportedCalls.indexOf(functionName) != -1 &&
      MiniAppExtension.callbackMap[key] &&
      MiniAppExtension.callbackMap[key].length > 0
    ) {
      console.log("SDK Received from CG frontend", event.data);
      callback = MiniAppExtension.callbackMap[key].shift();
      // delete args.requestId;
      callback(args);
    }
  },
  false
);