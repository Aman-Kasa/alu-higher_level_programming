#!/usr/bin/node

// Get all arguments from the command line, excluding the first two (node and script name)
const args = process.argv.slice(2).map(Number);

// If there are less than 2 arguments, print 0
if (args.length <= 1) {
  console.log(0);
} else {
  // Sort arguments in descending order and print the second largest
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
