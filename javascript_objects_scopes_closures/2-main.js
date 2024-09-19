#!/usr/bin/node

const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(`Instance width: ${r1.width} - height: ${r1.height}`);

const r2 = new Rectangle(2, -3);
console.log(`Instance width: ${r2.width} - height: ${r2.height}`);

const r3 = new Rectangle(3);
console.log(`Instance width: ${r3.width}`);

const r4 = new Rectangle(2, 0);
console.log(`Instance width: ${r4.width} - height: ${r4.height}`);

const r5 = new Rectangle();
console.log(`Instance width: ${r5.width} - height: ${r5.height}`);
