#!/usr/bin/node

const argument = process.argv;

const fs = require('fs');
fs.readFile(argument[2], (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
});
