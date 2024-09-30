#!/usr/bin/node
const request = require('request');

// Get the API URL from the command-line argument
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error); // Print the error if any
  } else {
    try {
      const films = JSON.parse(body).results; // Parse the JSON response
      const wedgeId = '18';
      let count = 0;

      // Loop through each film and check if Wedge Antilles (ID 18) is present
      for (const film of films) {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
          count++;
        }
      }

      console.log(count); // Print the count of movies Wedge Antilles appears in
    } catch (parseError) {
      console.log('Invalid JSON received from server');
    }
  }
});
