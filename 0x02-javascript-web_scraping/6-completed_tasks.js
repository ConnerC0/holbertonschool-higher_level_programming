#!/usr/bin/node

require('request')(process.argv[2], function (error, response, body){
    if (error) {
        console.error(error)
    } else {
        const completed = {};
        const JSONcontent = JSON.parse(body);
        for (let i = 0; i < JSONcontent.length; i++) {
            const id = JSONcontent[i].userID
            const finished = JSONcontent[i].completed;
            if (finished) {
                if (!completed[id]) {
                    completed[JSONcontent[i].userID] = 1;
                } else {
                    completed[JSONcontent[i].userID] += 1;
                }
            }
        }
        console.log(completed)
    }
});
