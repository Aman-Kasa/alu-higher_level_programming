#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check if both w and h are positive integers
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
    // Otherwise, do nothing (creates an empty object)
  }
}

module.exports = Rectangle;
