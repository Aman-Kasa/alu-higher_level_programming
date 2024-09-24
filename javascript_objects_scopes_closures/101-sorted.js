#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

for (const [userId, occurrences] of Object.entries(dict)) { // Get the number of occurrences and user ids
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}

console.log(newDict);
