#!/usr/bin/node

const request = require('request');

// Request URL
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);

  // convert request in to javascript oobject
  const object = JSON.parse(body);
  let count = 0;

  // iterate inside the list contining objects
  for (item of object.results) {
    const _list = item.characters;

    // iterate inside objects
    for (_string of _list) {
      if (_string.includes(18)) {
        count += 1;
      }
    }
  }
  console.log(count);
});
