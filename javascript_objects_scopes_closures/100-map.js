#!/usr/bin/node

const list = require('./100-data').list; // Import the list from 100-data.js
console.log(list); // Print the original list

const newList = list.map((value, index) => value * index); // Create a new array where each element is value * index
console.log(newList); // Print the new list
