#!/usr/bin/node

const SquareParent = require("./5-square");

class Square extends SquareParent {
  charPrint(c) {
    const char = c === undefined ? "X" : c;
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
