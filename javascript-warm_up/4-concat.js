#!/usr/bin/node

const process = require('process');
const variable = process.argv

if (variable.length > 3)
    console.log(variable[2] +' is '+ variable[3])
else
    console.log('undefine is undefine')