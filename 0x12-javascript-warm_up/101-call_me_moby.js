#!/usr/bin/node

function execute (x, theFunction) {
  for (let m = 0; m < x; m++) {
    theFunction();
  }
}
