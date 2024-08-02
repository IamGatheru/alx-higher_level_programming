#!/usr/bin/node

const fs = require('fs');
// Retrieve commandline arguments
const [,, filePath, content] = process.argv;

// Check if both arguments are provided
if (!filePath || !content) {
  console.error('Usage: node script.js <filePath> <content>');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error('An error occurred:', err);
    return;
  }
  console.log(`Content written to ${filePath}`);
});
