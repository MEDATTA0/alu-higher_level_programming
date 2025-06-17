#!/usr/bin/node

const request = require("request");
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const completed = {};

    for (const todo of todos) {
      if (todo.completed) {
        if (!completed[todo.userId]) {
          completed[todo.userId] = 0;
        }
        completed[todo.userId]++;
      }
    }

    console.log(completed);
  }
});
