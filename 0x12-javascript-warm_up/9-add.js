#!/usr/bin/node
function add (a, b) { return a + b; }
if (process.argv[2] && process.argv[3]) {
  const int1 = parseInt(process.argv[2], 10);
  const int2 = parseInt(process.argv[3], 10);
  console.log(add(int1, int2));
} else {
  console.log('NaN');
}
