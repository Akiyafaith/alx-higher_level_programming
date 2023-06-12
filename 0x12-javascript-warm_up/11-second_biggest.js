#!/usr/bin/node

function SecondBiggest (args) {
  if (args.length < 2) {
    return 0;
  }

  let Large = parseInt(args[2]);
  let Largest = parseInt(args[2]);

  for (let x = 3; x < args.length; x++) {
    const current = parseInt(args[x]);

    if (current > Large) {
      Largest = Large;
      Large = current;
    } else if (current > Largest && current < Large) {
      Largest = current;
    }
  }

  return Largest;
}
const Largest = SecondBiggest(process.argv);
console.log(Largest);
