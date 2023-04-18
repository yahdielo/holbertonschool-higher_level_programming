#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // print the squre with c and X if c is undefine
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let object = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.width; j++) {
        object += c;
      }
      if (i < this.width - 1) { object += '\n'; }
    }
    console.log(object);
  }
}
module.exports = Square;
