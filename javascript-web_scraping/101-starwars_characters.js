#!/usr/bin/node
const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

// Validate Movie ID
if (!movieId) {
  console.error('Missing Movie ID');
  process.exit(1);
}

// API URL for the specified movie
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie data
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film:', error);
    return;
  }

  const filmData = JSON.parse(body);
  
  // Check if the film exists
  if (!filmData.title) {
    console.error('Film not found');
    return;
  }

  // Extract character URLs
  const characterUrls = filmData.characters;

  // Function to fetch character names
  const fetchCharacterNames = (urls) => {
    let characterCount = 0;
    
    urls.forEach((url) => {
      request(url, (err, res, characterBody) => {
        if (err) {
          console.error('Error fetching character:', err);
          return;
        }
        
        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
        characterCount++;

        // Check if this was the last character to fetch
        if (characterCount === urls.length) {
          console.log('OK
