#!/usr/bin/node
const myVar = process.argv[2];
if (process.argv[2] && parseInt(myVar, 10)) {
  const intiger = parseInt(myVar, 10);
  console.log('My number:', intiger);
} else {
  console.log('Not a number');
}
