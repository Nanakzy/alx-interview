#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL to fetch the movie details from the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

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

  // Loop through each character URL to fetch and print the character's name
  characters.forEach(characterUrl => {
    // Make an HTTP GET request to fetch the character details
    request(characterUrl, (error, response, body) => {
      // Handle any errors that occur during the request
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the response body as JSON to get the character details
      const character = JSON.parse(body);
      // Print the character's name
      console.log(character.name);
    });
  });
});
