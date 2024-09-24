#!/usr/bin/node

// Import the dictionary from 101-data.js
const dict = require('./101-data.js').dict;

// Create an empty dictionary to store occurrences
const newDict = {};

// Loop through each key-value pair in the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId];  // Get the number of occurrences for each user id
  
  // If the occurrence is not already a key in newDict, add it
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  
  // Push the user id into the list of the corresponding occurrence
  newDict[occurrence].push(userId);
}

// Print the new dictionary
console.log(newDict);
