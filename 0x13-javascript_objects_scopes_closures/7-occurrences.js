#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let k = 0; k < list.length; k++) {
    if (list[k] === searchElement) {
      count++;
    }
  }

  return count;
};
