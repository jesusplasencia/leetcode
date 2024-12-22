const { Stack } = require("./Stack");

const myStack = new Stack();
myStack.fromArray([1, 3, 5, 7, 9, 0]);

console.log('Stack: ', JSON.stringify(myStack, null, 10));
console.log('Length: ', myStack.length);