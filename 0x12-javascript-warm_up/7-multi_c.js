#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
