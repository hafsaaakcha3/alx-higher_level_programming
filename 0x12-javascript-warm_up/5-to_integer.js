#!/usr/bin/node
const args = process.argv;
args[2] = parseInt(args[2]);

if (!isNaN(args[2]) && args.length === 3) {
  console.log('My number: ' + args[2]);
} else {
  console.log('Not a number');
}
