#!/usr/bin/node

require('request')('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function(error, response, body) {
    if (error) {
        console.error(error);
    } else {
        console.log(JSON.parse(body).title);
    }
});
