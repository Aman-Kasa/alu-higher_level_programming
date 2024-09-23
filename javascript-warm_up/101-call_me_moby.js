#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {  // Loop 'x' times
    theFunction();               // Call the function passed as argument
  }
};
