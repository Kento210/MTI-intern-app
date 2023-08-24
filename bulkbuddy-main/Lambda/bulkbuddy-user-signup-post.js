const { DynamoDBClient, PutItemCommand } = require("@aws-sdk/client-dynamodb");
const { marshall } = require("@aws-sdk/util-dynamodb");
const client = new DynamoDBClient({ region: "ap-northeast-1" });
const TableName = "team1_user";


exports.handler = async (event, context) => {
  const response = {
    statusCode: 200,
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify({ message: "" }),
  };

  
  const { userId, name, password, height, weight, age, calorie, targetWeight, targetDate ,gender} = JSON.parse(event.body);
  const param = {
    
    TableName, 
    Item: marshall({
      userId, 
      name, 
      password,
      height,
      weight,
      age,
      calorie,
      targetWeight,
      targetDate,
      gender,
      
    }),
  };

  const command = new PutItemCommand(param);

  try {
    await client.send(command);
    response.statusCode = 201;
    response.body = JSON.stringify({userId, name, height, weight, age, calorie, targetWeight, targetDate });
  } 
  catch (e) {
    response.statusCode = 500;
    response.body = JSON.stringify({
      message: "予期せぬエラーが発生しました。",
      errorDetail: e.toString(),
    });
  }

  return response;
};