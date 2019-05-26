from BetterXLRD.SpreadSheet import SpreadSheet
from Dijkstra.Graph import Graph
from Dijkstra.Edge import Edge
from Dijkstra.Vertex import Vertex
import DBConnector as DB
import json
# Ideas
# Use excel spreadsheets to store relationships between items
# Columns represent origins rows represent destinations
#    A   B  C
# A -1  -1  -1
# B  1  -1  -1
# C  4  1   -1
#
#
#

# Goals
#  ~ connect to MongoDB DONE
#  ~ display all information DONE
#  ~ figure out how to store nodes and verticies
#  ~ figure out how to read stored node and vertex data
#  ~ form graph from data from the Database
#  ~ run dijkstra's shortest path algorithm on database graph

# connect to databases
db1 = DB.connect("vertices", {'titles': ['name']})
db2 = DB.connect("edges", {'titles': ['weight','origin','destination']})

# create graph and initialize nodes
graph = Graph()
vertexnames = "A,B,C,D,E".split(",")
for v in vertexnames:
    graph.addVertex(v)

graph.addEdge(3, "A", "B")
graph.addEdge(4, "A", "C")
graph.addEdge(1, "B", "C")
graph.addEdge(2, "B", "D")
graph.addEdge(1, "D", "E")
graph.addEdge(7, "C", "E")

graph.printGraphInfo()

# @Output specifies where the vertices will be uploaded to
# @Graph specicifies the graph whose verticies will be uploaded
def uploadVertices(Graph, Output):
    vertices = Graph.VertexList
    for v in vertices:
        if Output.contains({'name':v.name}):
            print("Vertex {} already exists".format(v.name))
        else:
            Output.insert({'name': v.name})

# @Output specifies where the edges will be uploaded to
# @Graph specicifies the graph whose edges will be uploaded
def uploadEdge(Graph, Output):
    edges = Graph.EdgeList
    for e in edges:
        data = {'origin': e.startVertex.name, 'destination': e.targetVertex.name, 'weight': e.weight}
        if Output.contains(data):
            print("Edge already exists: ({}, {}, {})".format(e.startVertex.name,e.targetVertex.name,e.weight))
        else:
            Output.insert(data)
# @Source is a database containing data for vertices
# @Output is a graph object where vertices will be created using data from the Source
def downloadVerticies(Source, Output):
    vertices = Source.fetch_all_entries()
    for vertex in vertices:
        Output.addVertex(vertex['name'])

# @Source is a database containing data for edges
# @Output is a graph object where edges will be created using data from the Source
def downloadEdges(Source, Output):
    edges = Source.fetch_all_entries()
    for edge in edges:
        Output.addEdge(edge['weight'], edge['origin'], edge['destination'])

# uploadVertices(graph,db1)
# uploadEdge(graph,db2)
# graph2 = Graph()
# graph2.printGraphInfo()

# downloadVerticies(db1, graph2)
# ownloadEdges(db2, graph2)
# graph2.printGraphInfo()
# graph2.getVertex("A").printData()
# graph.getVertex("A").printData()
# graph2.calculateShortestPath(graph2.getVertex("A"))
# graph2.getShortestPathTo("E")

if __name__ == '__main__':
    print("this is essentialls like a public static void main(String[] args) {...} in java")
