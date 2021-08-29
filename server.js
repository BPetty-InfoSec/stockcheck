/**
 * Server for stock check app. Serves json file and web page, and triggers python scripts.
 */

// Import core http module and static module
const http = require('http');
const static = require('node-static');
// const fs = require('fs');
const port = 7777;

var stockFile = new(static.Server)(__dirname);

http.createServer(function(req, res) {
    file.serve(req,res);
}).listen(port)

console.log("Server listening on " + stockFile.address + ":" + stockFile.port);