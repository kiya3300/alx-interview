#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const FILMID = process.argv[2];

function doRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}

async function main (filmId) {
  const res = await doRequest(`${url}/${filmId}`);
  for (const character of res.characters) {
    const resCharcter = await doRequest(character);
    console.log(resCharcter.name);
  }
}

main(FILMID);
