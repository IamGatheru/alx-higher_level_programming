#!/usr/bin/node
const miss = 'Missing size';
const x = process.argv[2];
if (!parseInt(x)) {
  console.log(miss);
} else {
  for (let i = 0; i < x; i++) {
    let y = 0;
    let myVar = '';

    while (y < x) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}
