#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Initialize width and height only if w and h are positive integers
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Set width and height to undefined if invalid input
      this.width = undefined;
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;
