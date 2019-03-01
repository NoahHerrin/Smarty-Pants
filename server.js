const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
app.use("/public", express.static(__dirname + "/public"));
app.use(bodyParser.urlencoded({
  extended: true
}));

// Home route
app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
  console.log("New Connection");
});

app.listen(4000, function() {
  console.log("Starting Server");
});