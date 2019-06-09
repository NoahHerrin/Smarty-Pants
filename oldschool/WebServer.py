from BetterXLRD.SpreadSheet import SpreadSheet
from Dijkstra.Graph import Graph
from Dijkstra.Edge import Edge
from Dijkstra.Vertex import Vertex
import DBConnector as DB

import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('index.html', name = user)
@app.route('/')
def home(user):
   return "positive"

if __name__ == '__main__':
   app.run(debug = True)
