#!/usr/bin/node

const process = require('process');
const variable = process.argv;

let i = 0;

if (variable.length < 3) {
  console.log('Missing number of occurrences');
}
while (i < variable[2]) {
  console.log('C is fun');
  i++;
}
