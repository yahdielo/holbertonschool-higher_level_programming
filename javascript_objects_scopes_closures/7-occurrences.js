#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  // loop inside items
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
