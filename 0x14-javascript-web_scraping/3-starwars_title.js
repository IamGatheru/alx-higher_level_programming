#!/usr/bin/node

const request = require('request');

function getMovieTitleByEpisode (episodeNumber) {
  const url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.log('Error fetching data:', error);
      return;
    }
    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      console.log('Title:', data.title);
    } else {
      console.error('Failed to retrieve data:', response.statusCode);
    }
  });
}

const episodeNumber = process.argv[2];

if (episodeNumber) {
  getMovieTitleByEpisode(episodeNumber);
} else {
  console.error('Please provide an episode number.');
}
