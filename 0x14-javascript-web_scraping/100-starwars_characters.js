#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characterUrls = data.characters;
  for ( const characterUrl of characterUrls) {
    request.get(characterUrl, function (error, response, characterData) {
      if (error) {
        console.log(error);
      }
      const character = JSON.parse(characterData);
      console.log(character.name);
  });
  }
}); 
