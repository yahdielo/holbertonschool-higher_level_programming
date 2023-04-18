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

  print () {
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { square += 'x'; }
      if (i < this.height - 1) { square += '\n'; }
    }
    console.log(square);
  }
}
module.exports = Rectangle;
