#!/usr/bin/node

// Get the first and second arguments from the command line
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);

// Function that adds two integers
function add (a, b) {
  return a + b;
}

// Check if the arguments are valid numbers and print the result
console.log(add(a, b));
