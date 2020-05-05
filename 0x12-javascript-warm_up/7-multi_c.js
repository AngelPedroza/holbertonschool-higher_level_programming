#!/usr/bin/node
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
const array = 'C is fun';
const myVar = process.argv[2];
const intiger = parseInt(myVar, 10);
for (let i = 0; i < intiger; i++) {
  console.log(array);
}
