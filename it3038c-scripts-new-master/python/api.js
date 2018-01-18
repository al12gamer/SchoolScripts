var http = require("http");
var data = require("./widgets.json")

var server = http.createServer(function(req, res){
    if (req.url === "/") {
            res.writeHead(200, {"Content-Type":"text/json"});
                    res.end(JSON.stringify(data));
                        }
                            else if (req.url === "/blue") {
                                    listBlue(res);
                                        }
                                            else if (req.url === "/widgets") {
                                                    listWidgets(res);
                                                        }
                                                            else {
                                                                    res.writeHead(404, {"Content-Type": "text/plain"});
                                                                            res.end("Welp....Data not found");
                                                                                }
                                                                                });
                                                                                
                                                                                server.listen(3000);
                                                                                console.log("Server is listening on port 3000");
                                                                                
                                                                                function listBlue(res) {
                                                                                    var colorBlue = data.filter(function(item){
                                                                                            return item.color === "blue";
                                                                                                });
                                                                                                    res.end(JSON.stringify(colorBlue));
                                                                                                    }
                                                                                                    
                                                                                                    function listWidgets(res) {
                                                                                                        res.writeHead(200, {"Content-Type":"text/json"});
                                                                                                            res.end(JSON.stringify(data));
                                                                                                            }