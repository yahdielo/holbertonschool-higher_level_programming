#!/usr/bin/node

const process = require('process');
const variable = process.argv

i = 0

for (i in variable)

    if (i == 2)

        console.log(variable[i])

if (i == 1)
    console.log('No argument')