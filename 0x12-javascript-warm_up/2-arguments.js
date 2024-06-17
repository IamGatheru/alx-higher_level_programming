#!/usr/bin/node
const zero = 'No argument';
const one = 'Argument found';
const multi = 'Arguments found';
if (process.argv.length === 2) {
  console.log(zero);
} else if (process.argv.length === 3) {
  console.log(one);
} else {
  console.log(multi);
}
