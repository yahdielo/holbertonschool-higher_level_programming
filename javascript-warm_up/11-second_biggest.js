#!/usr/bin/node

const process = require('process');
const variable = process.argv;

function second_biggest(list)
{
    sorted_list = []
    if(variable.length <= 3) {
        return 0;
    }
    else
        sorted_list = variable.sort()
        return sorted_list[3]

}

result = second_biggest(variable)
console.log(result)