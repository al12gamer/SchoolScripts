var path = require("path");
var hello = "Hello from Node JS!"
console.log(`Printing Variable : ${hello}1);

console.log(__dirname);
console.log(__filename);

console.log(`Hello from ${path.basename(__filename)}`);