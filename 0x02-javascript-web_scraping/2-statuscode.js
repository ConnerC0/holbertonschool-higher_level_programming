#!/usr/bin/node

require('request')(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
