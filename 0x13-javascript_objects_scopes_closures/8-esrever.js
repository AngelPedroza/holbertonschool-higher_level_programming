#!/usr/bin/node
exports.esrever = function (list) {
  let fin = list.length - 1;
  let tmp = '';
  for (let i = 0; i < list.length; i++) {
    if (i >= fin) { return list; }

    tmp = list[i];
    list[i] = list[fin];
    list[fin] = tmp;

    fin -= 1;
  }
};
