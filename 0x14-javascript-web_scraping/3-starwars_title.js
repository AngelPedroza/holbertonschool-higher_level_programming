#!/usr/bin/node
const request = require('request');
if (0 < process.argv[2] && process.argv[2] < 7) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
  request.get(url, function (err, response, body) {
    if (err) { console.log(err); } else {
      console.log(JSON.parse(body).title);
    }
  });
}
