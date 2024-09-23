#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

// Add an incr function to myObject
myObject.incr = function () {
  this.value++; // Increment the value property of myObject
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
