#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (error, response, body) => {
  // if i get error , console loge it
  if (error) console.log(error);

  // converting result from the request in to a javascript object
  const obj = JSON.parse(body);

  // i can call value of a object by passing the key as mathod to object
  console.log(obj.title);
});
