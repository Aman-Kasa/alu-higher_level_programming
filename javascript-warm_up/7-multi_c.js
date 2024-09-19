#!/usr/bin/node

// Get the first argument from the command line
const args = process.argv;

// Convert the first argument to an integer
const x = parseInt(args[2]);

// Check if the argument is a valid number
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
