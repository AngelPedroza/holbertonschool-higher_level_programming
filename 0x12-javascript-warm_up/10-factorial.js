#!/usr/bin/node
const factorial = function fac (n) { return n < 2 ? 1 : n * fac(n - 1); };
if (process.argv[2]) {
  const intiger = parseInt(process.argv[2], 10);
  console.log(factorial(intiger));
} else {
  console.log(factorial(1));
}
