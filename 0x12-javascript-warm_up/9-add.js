#!/usr/bin/node
const count = process.argv.length;
if (count < 3) {
  console.log('NaN');
} else {
  const g = Number(process.argv[2]);
  const h = Number(process.argv[3]);
  console.log(add(g, h));
}
function add (a, b) {
  return a + b;
}
