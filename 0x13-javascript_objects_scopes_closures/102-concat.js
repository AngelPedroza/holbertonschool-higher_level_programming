#!/usr/bin/node
const fs = require('fs');
const text1 = fs.readFileSync(process.argv[2], 'utf8');
const text2 = fs.readFileSync(process.argv[3], 'utf8');
const fString = text1.toString() + '\n' + text2.toString() + '\n';
fs.writeFile(process.argv[4], fString, (err) => { if (err) throw err; });
