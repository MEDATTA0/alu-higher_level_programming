#!/usr/bin/node

const request = require("request");
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body);
    let count = 0;
    for (const film of data.results) {
      for (const character of film.characters) {
        if (character.includes("/18/")) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
