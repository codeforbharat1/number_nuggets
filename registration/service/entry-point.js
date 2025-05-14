const model = require('../../model');
const { Text, Button } = require('../../utils/message-types');
const { getQuestionOptionsArray } = require('../../utils/helpers');
const logger = require('../../utils/logger');
const entryPoint = async ({
  waNumber,
  userMobile,
  userContext,
  userMedium,
  userMessage,
  isReturn = false,
}) => {
  const responseMessage = [];
  const questionOptionsArray = [];
  // const [welcomeString, continueString] = await Promise.all([
  //   model.getString(`ST001`, userMedium),
  //   model.getString(`ST002`, userMedium),
  // ]);
  // questionOptionsArray.push(continueString);
  // responseMessage.push(
  //   new Button(
  //     new Text(welcomeString),
  //     getQuestionOptionsArray(questionOptionsArray)
  //   )
  // );

  userContext.stepName = 'entryPoint';
  // userContext.stepData = { questionOptions: [] };

if (userMessage != null && !isNaN(userMessage)) {
  const number = parseInt(userMessage, 10); // Convert to number safely

  // Call Numbers API
  const response = await fetch(`http://numberapi.com/${number}?json`);
  const data = await response.json(); // Parse JSON

  responseMessage.push(new Text(data.text)); // Push trivia text
  // responseMessage.push(new Text("Please enter a valid number."));
  // const thankYouString = await model.getString('ST002', userMedium);

  // responseMessage.push(
  //   new Button(
  //     new Text(thankYouString),
  //     getQuestionOptionsArray(['string1', 'string2'])
  //   )
  // );

  model.sendMessage(waNumber, userMobile, responseMessage).catch((err) =>
    logger.error('Send Message Failure ', {
      waNumber,
      userMobile,
      responseMessage,
      err: model.constructError(err),
    })
  );
  return;
} else {
  
  model.sendMessage(waNumber, userMobile, responseMessage).catch((err) =>
    logger.error('Send Message Failure ', {
      waNumber,
      userMobile,
      responseMessage,
      err: model.constructError(err),
    })
  );
}



  // await model.updateUserContext(userMobile, userContext);
  // model.sendMessage(waNumber, userMobile, responseMessage).catch((err) =>
  //   logger.error('Send Message Failure ', {
  //     waNumber,
  //     userMobile,
  //     responseMessage,
  //     err: model.constructError(err),
  //   })
  // );
};

module.exports = entryPoint;
