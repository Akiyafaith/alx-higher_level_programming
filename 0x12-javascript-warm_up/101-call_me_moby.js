#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (let m = 0; m < x; m++) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
