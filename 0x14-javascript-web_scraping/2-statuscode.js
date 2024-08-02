#!/usr/bin/node
const request = require('request');
const [,, url] = process.argv;

function main (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error(`An error occurred: ${error.message}`);
      return;
    }
    console.log(`code: ${response.statusCode}`);
  });
}

if (!url) {
  console.log('Usage: node script.js <URL>');
  process.exit(1);
}
main(url);
