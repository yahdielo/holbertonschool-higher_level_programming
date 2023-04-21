#!/usr/bin/node

const request = require('request');

// Request URL
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request(url, (error, response, body) => {
  // if error return it
  if (error) console.log(error);

  fs.writeFile(file, body, (err) => {
    if (err) throw err;
  });
});
