#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const newDict = {};
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      if (newDict[todos[i].userId] === undefined) { newDict[todos[i].userId] = 0; }
      if (todos[i].completed === true) { newDict[todos[i].userId] += 1; }
    }
    console.log(newDict);
  }
});
