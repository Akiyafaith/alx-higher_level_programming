#!/usr/bin/node

function addMeMaybe (num, theFunction) {
  num++;
  theFunction(num);
}

module.exports = {
  AddMeMaybe: addMeMaybe
};
