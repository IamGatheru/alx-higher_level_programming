#!/usr/bin/node
const fail = 'Missing number of occurrences';
const count = process.argv.length;
const argument1 = process.argv;

if (count <= 2 || argument1[1] < 0) {
  console.log(fail);
}
for (let x = 0; x < argument1[2]; x++) {
  console.log(('C is fun'));
}
