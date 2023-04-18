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

  // class method to print rectangle
  print () {
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { square += 'X'; }
      if (i < this.height - 1) { square += '\n'; }
    }
    console.log(square);
  }

  // method to rotate rectangle
  rotate () {
    const new_h = this.height;
    const new_w = this.width;
    this.width = new_h;
    this.height = new_w;
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { square += 'X'; }
      if (i < this.height - 1) { square += '\n'; }
    }
    console.log(square);
  }

  // method to dobke the size of rectangle
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { square += 'X'; }
      if (i < this.height - 1) { square += '\n'; }
    }
    console.log(square);
  }
}
module.exports = Rectangle;
