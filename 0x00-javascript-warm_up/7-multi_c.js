#!/usr/bin/node
const argValue = process.argv[2];
if (isNaN(argValue)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = argValue; i > 0; i--) {
    console.log('C is fun');
  }
}
