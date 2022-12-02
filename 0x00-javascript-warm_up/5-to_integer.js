#!/usr/bin/node
const argValue = process.argv[2];
if (isNaN(argValue)) {
  console.log('Not a number');
} else {
  console.log('My number:', argValue);
}
