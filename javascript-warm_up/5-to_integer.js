#!/usr/bin/node

const process = require('process');
const variable = process.argv


if (variable.length == 2)
    console.log('Not a number')

if (typeof variable[2] === 'number' &&
    !Number.isNaN(variable[2]) &&
    !Number.isInteger(variable[2])
    ) {
        console.log('My number: '+ variable[2])
    }
    else
        console.log('My number: ' + variable[2])
        
if (variable.length == 3)
    if (isNaN(variable[2])== true)
        console.log('Not a number')