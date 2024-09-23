#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number); // Increment the number and call the function with the new value
};
