#!/usr/bin/node
const argValue = process.argv[2];
if (argValue === undefined) {
  console.log('No argument');
} else {
  console.log(argValue);
}
