console.log(process.argv);

if (process.argv.length <= 2) {
    console.log("USAGE: " + __filename + " IPADDR")
}

var ip = process.argv[1];
console.log(`Argument 2: ${ip}`);