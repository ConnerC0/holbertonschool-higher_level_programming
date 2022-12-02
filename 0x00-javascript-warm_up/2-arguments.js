#!/usr/bin/node
const argSize = process.argv.length;
if (argSize === 2) {
  console.log('No argument');
} else if (argSize === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
