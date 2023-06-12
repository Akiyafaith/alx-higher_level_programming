#!/usr/bin/node
const argm = process.argv[2];
const convertedNum = parseInt(argm);

if (!isNaN(convertedNum)) {
  console.log('My number: ' + convertedNum);
} else {
  console.log('Not a number');
}
