#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const wedgeAntillesID = 18;

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body
  const films = JSON.parse(body).results;
  let count = 0;

  // Loop through each film and check for Wedge Antilles
  films.forEach((film) => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesID}/`)) {
      count++;
    }
  });

  // Print the count of films featuring Wedge Antilles
  console.log(count);
});
