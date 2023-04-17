#!/usr/bin/node

const process = require('process');
const variable = process.argv;

function second_biggest (list) {
  let sorted_list = [];
  if (variable.length <= 3) {
    return 0;
  } else { sorted_list = variable.sort(); }
  return sorted_list[sorted_list.length - 2];
}
let result = 0;
result = second_biggest(variable);
console.log(result);
