http.createServer(function (req, res) {
    var prompt = generation.prompt('bike bell')
    res.write(prompt);
    res.end();
}).listen(8080)