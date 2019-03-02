var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'closet'
});


connection.connect();
//var query = "INSERT INTO clothing ( id , type , color) VALUES ('1', 'Shirt', 'Blue')";
//addItem("SHIRT", "GREEN");
//addItem("JEANS", "BLACK");
setTimeout(function() {
  printTable();

}, 2000);

//Inserts new item into database
function addItem(type, color) {
  var sql = "INSERT INTO clothing ( type , color) VALUES (" +
    "" + connection.escape(type) + " , " + connection.escape(color) + ")";
  let query = connection.query(sql);
  query.on('error', function(err) {
    throw err;
  });
}

function printTable() {
  var query = connection.query("SELECT * FROM clothing");

  query.on('error', function(err) {
    throw err;
  });

  query.on('fields', function(fields) {
    //this field was returning null
    //console.log(fields.name);
  });

  query.on('result', function(row) {
    if (row == null) return;
    var obj = JSON.parse(JSON.stringify(row));
    console.log("ID: " + row.id + ", TYPE: " + row.type + ", COLOR: " + row.color);
  });
}