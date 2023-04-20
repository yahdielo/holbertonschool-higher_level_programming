#!/usr/bin/node

let argument = process.argv;

const fs = require('fs')
fs.readFile(argument[2], (err, inputD) => {
    if (err) throw err;
    console.log(inputD.toString());
})

