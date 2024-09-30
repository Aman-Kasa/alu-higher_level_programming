#!/usr/bin/node
const request = require('request');

// Get the URL from the first command-line argument
const url = process.argv[2];

// Make a GET request to the URL
request(url, (error, response) => {
  if (error) {
    console.log(error); // Print the error if any
  } else {
    console.log(`code: ${response.statusCode}`); // Print the status code
  }
});
