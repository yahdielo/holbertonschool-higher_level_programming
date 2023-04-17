#!/usr/bin/node

const process = require('process');
const variable = process.argv;

let square = '';
if (variable.length <= 2 || isNaN(variable[2]) === true) { console.log('Missing size'); }

for (let i = 0; i < variable[2]; i++) {
  for (let j = 0; j < variable[2]; j++) {
    square += 'X';
  }
  if (i < variable[2] - 1) { square += '\n'; }
}
if (square !== '') { console.log(square); }
