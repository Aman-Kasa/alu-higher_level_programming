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

  // Function to fetch character names in order
  const fetchCharacterNames = (urls) => {
    let characterPromises = urls.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (err, res, characterBody) => {
          if (err) {
            reject('Error fetching character:', err);
            return;
          }

          const characterData = JSON.parse(characterBody);
          resolve(characterData.name);
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach(name => console.log(name));
      })
      .catch((err) => {
        console.error(err);
      });
  };

  // Fetch character names in the order they are listed
  fetchCharacterNames(characterUrls);
});
