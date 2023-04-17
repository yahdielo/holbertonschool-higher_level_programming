#!/usr/bin/node

const process = require('process');
const variable = process.argv

if (variable.length == 3)
    console.log('Arguments found')
else
    console.log('No arguements')