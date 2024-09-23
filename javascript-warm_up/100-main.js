#!/usr/bin/node
myVar = 89;                // Declare a global variable myVar and set it to 89
require('./100-let_me_const');  // Load the module 100-let_me_const.js
console.log(myVar);         // Output the value of myVar after the module modifies it
