#!/usr/bin/node
const request = require('request');

// Function to fetch characters from a Star Wars movie
const fetchCharacters = (movieId) => {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  // Request to get the movie data
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const movieData = JSON.parse(body);
    if (!movieData.title) {
      console.log('Movie not found.');
      return;
    }

    const characters = movieData.characters;

    // Fetch character names in the order they are listed
    characters.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
          return;
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  });
};

// Get the movie ID from command line arguments and call the function
const movieId = process.argv[2];
fetchCharacters(movieId);
