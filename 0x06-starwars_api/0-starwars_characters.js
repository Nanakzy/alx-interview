#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL to fetch the movie details from the Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make an HTTP GET request to fetch the movie details
request(url, (error, response, body) => {
  // Handle any errors that occur during the request
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body as JSON to get the film details
  const film = JSON.parse(body);
  // Get the list of character URLs from the film details
  const characters = film.characters;

  // Fetch all characters in the correct order and display their names
  const fetchCharacter = (index) => {
    if (index >= characters.length) return;

    // Make an HTTP GET request to fetch the character details
    request(characters[index], (error, response, body) => {
      // Handle any errors that occur during the request
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the response body as JSON to get the character details
      const character = JSON.parse(body);
      // Print the character's name
      console.log(character.name);

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  };

  // Start fetching characters from the first one
  fetchCharacter(0);
});
