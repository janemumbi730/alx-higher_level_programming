#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let i = num;
  while (i > 0) {
    console.log('X'.repeat(num));
    i--;
  }
}
