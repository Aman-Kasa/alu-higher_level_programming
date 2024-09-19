#!/usr/bin/node

// Get the argument from the command line and convert to an integer
const n = parseInt(process.argv[2]);

// Recursive function to calculate factorial
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Print the factorial result
console.log(factorial(n));
