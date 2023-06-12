#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!isNaN(size)) {
  if (size > 0) {
    for (let m = 0; m < size; m++) {
      console.log('X'.repeat(size));
    }
  } else {
    console.log('Size must be a positive number');
  }
} else {
  console.log('Missing size');
}
