#!/usr/bin/node

const fs = require('fs');

// Get the file paths from command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Read contents of fileA and fileB
const dataA = fs.readFileSync(fileA, 'utf8');
const dataB = fs.readFileSync(fileB, 'utf8');

// Concatenate the contents of both files and write to fileC
fs.writeFileSync(fileC, dataA + dataB);
