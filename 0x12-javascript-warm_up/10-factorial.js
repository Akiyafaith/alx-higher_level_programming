#!/usr/bin/node

function factorial (q) {
  if (isNaN(q)) {
    return 1;
  }
  if (q === 0) {
    return 1;
  }
  return q * factorial(q - 1);
}

const num = parseInt(process.argv[2]);

const rslt = factorial(num);
console.log(rslt);
