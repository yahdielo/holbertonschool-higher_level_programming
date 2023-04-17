#!/usr/bin/node

const process = require('process');
const variable = process.argv;

function factorial (n) {
  if (isNaN(n) === true) { return 1; }

  if (n === 0 || n === 1) { return 1; } else {
    return n * factorial(n - 1);
  }
}
let answer = 0;
answer = factorial(variable[2]);
console.log(answer);
