#!/usr/bin/node
const myVar = process.argv[2];
if (process.argv[2] && parseInt(myVar, 10)) {
  const array = 'x';
  const intiger = parseInt(myVar, 10);
  for (let i = 0; i < intiger; i++) {
    for (let j = 0; j < intiger; j++) {
      process.stdout.write(array);
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
