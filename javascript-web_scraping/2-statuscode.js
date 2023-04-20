#!/usr/bin/node

const argument = process.argv

let url = argument[2];

async function request() {
try {
    const response = await fetch(url);

    console.log('response.status: ', response.status);
    } catch (err) {
        console.log(err);
    }
}

request();