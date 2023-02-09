#!/usr/bin/node
const request = require('request');
/**
 *  @param argv
 *  @returns string
 */

let arg = process.argv.slice(2);
let url = 'https://swapi-api.alx-tools.com/api/films/'+ arg[0];

let characters =[];
let characterNames =[];

/**
 * uses the promises api
 */

const getCharacters =  async () => {
    await new Promise( resolve => request(url , (err, res, body) => {
        if (err || res.statusCode !== 200) {
            console.error('error', err, '| statusCode' , res.statusCode)
        }else {
            let chars = JSON.parse(body);
          characters = chars.characters;
          resolve();
      }
    }))
};

const getCharactersNames = async () => {
    if (characters.length > 0) {
        for (let character in characters) {
            await new Promise ( resolve => request(character, (err, res, body) => {
                if (err || res.statusCode !== 200) {
                    console.error('error', err ,'| statusCode' , res.statusCode)
                }else {
                  let person = JSON.parse(body);
                  characterNames.push(person.name);
                  resolve();
                }
            }))
        }
    } else {
        console.error('Error: Got no Characters for check your internet connection other');
    }
};

const getNames = async () => {
    await getCharacters()
    await getCharactersNames()

    //print the names
    for(let charName in characterNames) {
        if (charName === characterNames[characterNames.length - 1]){
            process.stdout.write(charName);
        }else{
            process.stdout.write(charName + '\n');
        }
    }
};

getNames();
