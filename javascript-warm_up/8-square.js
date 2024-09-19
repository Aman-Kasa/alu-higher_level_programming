#!/usr/bin/node

// Get the first argument from the command line
const args = process.argv;
const size = parseInt(args[2]);

// Check if the argument is a valid number
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Use a loop to print the square of 'X'
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
