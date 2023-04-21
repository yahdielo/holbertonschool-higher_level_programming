#!/usr/bin/node

const request = require('request')
 
// Request URL
let url = process.argv;
request(url[2], (error, response, body) => {
    // Printing the error if occurred
    if (error) console.log(error)
 
    // Printing status code
    console.log('code:',response.statusCode);
});