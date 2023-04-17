#!/usr/bin/node

const process = require('process');
const variable = process.argv

if (variable.length > 3)
    console.log('Arguments found')
if (variable.length == 3)
    console.log('Argument found')
if (variable.length < 3)
    console.log('No arguement')