#!/usr/bin/node

const process = require('process');
const variable = process.argv;

function add(a, b)
{
    if (isNaN(a) === true && isNaN(b) === true)
        console.log('NaN')
    else
        console.log(Number(a) + Number(b))
}

result = add(variable[2], variable[3])

