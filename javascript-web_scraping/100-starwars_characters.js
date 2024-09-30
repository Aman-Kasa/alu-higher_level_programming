#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL for the specific movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the API to retrieve movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if one occurred
    return;
  }

  // Parse the response body to get movie data
  const movieData = JSON.parse(body);

  // Check if the movie was found
  if (movieData.title) {
    // Loop through the characters array
    movieData.characters.forEach(characterUrl => {
      // For each character URL, make a request to get character details
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError); // Print the error if one occurred
          return;
        }

        // Parse character data and print the character name
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  } else {
    console.log('Movie not found.'); // Handle case where movie ID is invalid
  }
});
