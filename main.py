from flask import Flask
import http.client
##import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Python Mobile App!"

@app.route("/Signup")
def signup():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{   \n    \"name\": \"UBS Merchant\",\n    \"email\": \"alokdiwan@gmail.com\",\n    \"password\": \"Password@1234\"\n}"
    headers = {}
    conn.request("POST", "/api/merchants", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route("/Create-Mini-App")  
def create_mini_app():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"email\": \"<mini-app-email>\",\n    \"configuration\": {\n        \"type\": \"WEB\",\n        \"name\": \"<mini-app-name>\",\n        \"category\": \"<category of the mini-app>\"\n    }\n}"
    headers = {}
    conn.request("POST", "/api/mini-apps", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/verify-mini-app')
def verify_mini_app():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    url = "https://v1-api.swiftchat.ai/api/mini-apps/verify"
    payload = "{\n    \"email\": \"abc@xyz.com\",\n    \"otp\": \"123456\",\n    \"country_code\": \"IN\"\n}"
    headers = {}
    conn.request("POST", "/api/mini-apps/verify", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/get-mini-apps')
def get_mini_app_details():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/merchants/<merchant-id>/mini-apps", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/mini-apps/configuration')
def get_mini_app_details_by_id():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/mini-apps/{{Mini-App-ID}}/configuration", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/mini-apps/configuration/update')   
def update_mini_app_configuration():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"name\": \"<mini-app-name>\",\n    \"category\": \"<mini-app-category>\",\n    \"description\": \"<description>\",\n    \"customer_support_email\": \"<support-email>\",\n    \"customer_support_phone\": \"<support-phone-number>\",\n    \"launch_url\": \"https://xyzabc.com\"\n}"
    headers = {}
    conn.request("PATCH", "/api/mini-apps/{{Mini-App-ID}}/configuration", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/mini-apps/get-shareable-link')
def get_mini_app_shareable_link():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/mini-apps/{{Mini-App-ID}}/shareable-link", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/merchant-login')
def get_merchant_login():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"email\": \"alokdiwan@gmail.com\",\n    \"password\": \"Password@1234\"\n}"
    headers = {}
    conn.request("POST", "/api/merchants/login", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/send-text-message')
def send_text_message():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"to\": \"<recepient-mobile>\",\n    \"type\": \"text\",\n    \"text\": {\n        \"body\": \"Hello\"\n    }\n}"
    headers = {}
    conn.request("POST", "/api/bots/<bot-id>/messages", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/create-text-template')
def create_text_template():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"name\": \"Test Template\",\n    \"category\": \"Marketing\",\n    \"language\": \"en\",\n    \"components\": [\n        {\n            \"type\": \"body\",\n            \"parameters\": [\n                {\n                    \"type\": \"text\",\n                    \"text\": \"Hello\"\n                }\n            ]\n        }\n    ]\n}"
    headers = {}
    conn.request("POST", "/api/bots/<bot-id>/messages/templates/text", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/merchant-details')
def get_merchant_details():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/merchants/<merchant-id>", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

@app.route('/merchant-credentials')
def get_merchant_credentials(): 
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/merchants/<merchant-id>/credentials", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


@app.route('/merchant-credentials/configuration')
def get_merchant_credentials_configuration(merchant_id):
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", f"/api/merchants/{merchant_id}/credentials/configuration", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

@app.route('/merchants/api-key/otp')
def  get_API_key_OTP(merchant_id, bot_id):
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", f"/api/merchants/{merchant_id}/api-key/otp", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

@app.route('/merchants/api-key/otp/verify')
def verfiy_API_key_OTP(merchant_id):
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", f"/api/merchants/{merchant_id}/api-key/otp", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")
    
@app.route('/merchant-configuration')
def get_merchant_configuration():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/merchants/<merchant-id>/configuration", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

@app.route('/bot-details')
def get_bot_details():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/merchants/<merchant-id>/bots", payload, headers)
    res = conn.getresponse()
    data = res.read()    
    return data.decode("utf-8")

@app.route('/bot-configuration')
def get_configuration():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/bots/<bot-id>/configuration", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

@app.route('/update-bot-configuration')
def update_configuration():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"name\": \"Test Bot\",\n    \"category\": \"Education\",\n    \"description\": \"Closing the gap in educational achievement for children and youth in India.\",\n    \"welcome_text\": \"Welcome to Test Bot.\",\n    \"allow_user_media\": true,\n    \"customer_support_email\": \"support@test.com\",\n    \"customer_support_phone\": \"+91XXXXXXXXXX\",\n    \"allow_custom_response\": false,\n    \"persistent_menu\": {\n        \"buttons\": [\n            {\n                \"id\": 1,\n                \"body\": \"Add Student\",\n                \"icon\": \"registration\",\n                \"reply\": \"I want to add another profile.\"\n            },\n            {\n                \"id\": 2,\n                \"body\": \"Change Medium\",\n                \"icon\": \"edit-registration\",\n                \"reply\": \"Change my medium of instruction.\"\n            }\n        ]\n    },\n    \"text_to_speech\": true\n}"
    headers = {}
    conn.request("PATCH", "/api/bots/<bot-id>/configuration", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

@app.route('/update-webhook_url')
def update_webhook_url():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"webhook_url\": \"https://test.com/webhook\"\n}"
    headers = {}
    conn.request("PUT", "/api/bots/<bot-id>/webhook-url", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def get_webhook_url():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/bots/<bot-id>/webhook-url", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def get_shareable_link():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("GET", "/api/bots/<bot-id>/shareable-link", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def create_bot():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"mobile\": \"+919892943716\",\n    \"configuration\": {\n        \"name\": \"Test Bot\",\n        \"category\": \"Education\"\n    }\n}"
    headers = {}
    conn.request("POST", "/api/bots", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def verify_bot():
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = "{\n    \"mobile\": \"+91XXXXXXXXXX\",\n    \"otp\": \"123456\"\n}"
    headers = {}
    conn.request("POST", "/api/bots/verify", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def delete_bot(): 
    conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    payload = ''
    headers = {}
    conn.request("DELETE", "/api/bots/<bot-id>", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8")) 

if __name__ == '__main__':
    
    #Testing Merchant API
    get_merchant_login()
    get_merchant_details()

    #Testing Bot API
    create_bot()
    verify_bot()
    get_bot_details()
    get_configuration()
    get_webhook_url()
    get_shareable_link()
    update_configuration()
    update_webhook_url()
    send_text_message()
    create_text_template() 
    #delete_bot()

    #Testing Mini-app API
    create_mini_app()
    verify_mini_app()
    get_mini_app_details()
    get_mini_app_details_by_id()
    update_mini_app_configuration()
    get_mini_app_shareable_link()
    
    #Testing Numbers API
    ##conn = http.client.HTTPSConnection("v1-api.swiftchat.ai")
    ##payload = "{\n    \"mobile\": \"+919892943716\",\n    \"configuration\": {\n        \"name\": \"Test Bot\",\n        \"category\": \"Education\"\n    }\n}"
    conn = http.client.HTTPConnection("numbersapi.com");
    payload = "32";
    #headers = {}
    headers = {'Content-type': 'application/json'}
    #conn.request("POST", "http://numbersapi.com/42", payload, headers)
    conn.request("GET", "http://numbersapi.com/42/trivia",payload, headers)
    ##url = f"http://numbersapi.com/{number}/{type}"
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    #Inorder to get the number from user
    number = input("Enter a number: ")
    if number.isdigit():
      number = int(number)
      fact_type = input("Enter fact type (trivia, math, date, year, or leave empty for trivia): ").lower()
    
      if fact_type in ('trivia', 'math', 'date', 'year', ''):
        if fact_type == '':
          fact_type = 'trivia'
        ##payload = number
        fact = conn.request("GET", "http://numbersapi.com/"+ str(number),payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
      else:
        print("Invalid fact type entered.")
    else:
      print("Invalid input. Please enter a valid number.")


    app.run();
    
