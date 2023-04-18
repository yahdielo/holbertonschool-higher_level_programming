#!/usr/bin/node

// clas  declaration
class Rectangle {
  constructor (w, h) {
    if (isNaN(w) === true || w < 0 || isNaN(h) === true || h < 0) {
      return 'Rectangle {}';
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
