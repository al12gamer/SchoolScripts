var http = require("http");
var fs = require("fs");
var os = require("os");
var uptime = os.uptime();

function convertMS(ms) {
    var d, h, m, s;
    s = Math.floor(ms / 1);
    m = Math.floor(s / 60);
    s = s % 60;
    h = Math.floor(m / 60);
    m = m % 60;
    d = Math.floor(h / 24);
    h = h % 24;
    return {d: d, h: h, m: m, s: s}
}

var interfaces = os.networkInterfaces();
var addresses = [];
for (var k in interfaces) {
    for (var k2 in interfaces[k]) {
        var address = interfaces[k][k2];
        if (address.family === 'IPv4' && !address.internal) {
            addresses.push(address.address);
        }
    }
}
var server = http.createServer(function(req, res){

    if (req.url === "/") {

    fs.readFile("./public/index.html", "UTF-8", function(err, body){
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(body);
    });

}

else if(req.url.match("/sysinfo")) {

    myHostName=os.hostname();
    myUpTime=(convertMS(uptime));
    myCPUs=os.cpus().length;
    myMEM=((os.totalmem())/1048576) + "MB";
    myFreedom=((os.freemem())/1048576) + "MB";
    

    html=`
    <!DOCTYPE html>
    <html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${addresses}</p>
            <p>Server Uptime: ${myUpTime}</p>
            <p>Total Memory: ${myMEM}</p>
            <p>Free Memory: ${myFreedom}</p>
            <p>CPUs: ${myCPUs} </p>
            </body>

    </html>
`

    res.writeHead(200, {"Content-Type": "text/html"});

    res.end(html);

}

else {
    res.writeHead(404, {"Content-Type": "text/html"});
    res.end("404 File Not Found");
    }
});

server.listen(3000);

console.log("Server is listening on port 3000");