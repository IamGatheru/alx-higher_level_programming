#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath ||!content) {
	console.error('Please provide a file path and the content to write.');
	process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (err) => {
	if (err) {
		console.error ('Error writing file:', err);
		return;
	}
	console.log('File written successfully');
});
