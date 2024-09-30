#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error); // Print error if there's any
  } else {
    // Write the body of the response to the file in UTF-8
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err); // Print error if file writing fails
      }
    });
  }
});
