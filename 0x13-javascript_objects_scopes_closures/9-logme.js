#!/usr/bin/node
exports.logMe = function (item) {
  if (this.count === undefined) { this.count = 0; }
  this.count++;
  console.log(this.count + ': ' + item);
};
