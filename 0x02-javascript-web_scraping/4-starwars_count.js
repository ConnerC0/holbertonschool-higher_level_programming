#!/usr/bin/node

require('request')(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const JSONdata = JSON.parse(body).results;
    let i = 0;
    for (const m in JSONdata) {
      const characters = JSONdata[m].characters;
      for (const charI in characters) {
        if (characters[charI].includes('/18/')) {
          i += 1;
        }
      }
    }
    console.log(i);
  }
});
