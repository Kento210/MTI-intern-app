// このエンドポイントにおいては、非同期である必要はないが、ほとんどのAPIは非同期であるためasyncハンドラで記述している。
exports.handler = async (event, context) => {
  const response = {
    statusCode: 200,
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify({ message: "" }),
  };

  const rbody = JSON.parse(event.body);
  response.body = JSON.stringify(rbody);

  return response;
};
