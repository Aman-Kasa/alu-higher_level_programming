#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Make a GET request to the Star Wars API with the provided movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error); // Print the error if any
  } else {
    const data = JSON.parse(body); // Parse the JSON response
    console.log(data.title); // Print the movie title
  }
});
