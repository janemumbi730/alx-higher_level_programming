#!/usr/bin/node

const movieId = process.argv[2];


const urlReq = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const request = require('request');

request(urlReq, (error, response, body) => {
  if (error) throw error;
  response = JSON.parse(body);
  const characters = response.characters;

  characters.forEach((value, ind) => {

    request(value, (error, response, body) => {
      if (error) throw error;
      const char = JSON.parse(body);
      console.log(char.name);
    });
  });
});
