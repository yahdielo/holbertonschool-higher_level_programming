#!/usr/bin/node

const process = require('process');
const variable = process.argv;

let square = '';
for (let i = 0; i < variable[2]; i++) {
  for (let j = 0; j < variable[2]; j++) {
    square += 'x';
  }
  square += '\n';
}
console.log(square);
