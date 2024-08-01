#!/usr/bin/node

const fs = require('fs');
// Retrieve commandline arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both arguments are provided
if (!filePath || !content) {
  console.error('Please provide a file path and the content to write.');
  process.exit(1);
}
//Write the string to file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log('Error writing file:', err);
    return;
  }
  console.log('File written successfully');
});
