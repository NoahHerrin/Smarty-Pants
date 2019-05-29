from Dijkstra.Graph import Graph
from Dijkstra.Edge import Edge
from Dijkstra.Vertex import Vertex
import DBConnector as DB

class SmartyPants(object):
    def __init__(self):
        self.vertices = DB.connect("vertices", {'titles': ['name']})
        self.edges = DB.connect("edges", {'titles': ['weight','origin','destination']})
    def downloadGraph(self):
        graph = Graph()
        vertices = self.downloadVertices(graph)
        edges = self.downloadEdges(graph)
        return graph
    def uploadVertices(self, Graph, Output):
        vertexList = Graph.VertexList
        for v in verexList:
            if Output.contains({'name':v.name}):
                print("Vertex {} already exists".format(v.name))
            else:
                Output.insert({'name': v.name})

    # @Output specifies where the edges will be uploaded to
    # @Graph specicifies the graph whose edges will be uploaded
    def downloadEdges(self, Output):
        edgeList = self.edges.fetch_all_entries()
        for edge in edgeList:
            Output.addEdge(edge['weight'], edge['origin'], edge['destination'])

    def uploadEdge(self, Graph, Output):
        edgLists = Graph.EdgeList
        for e in edgeList:
            data = {'origin': e.startVertex.name, 'destination': e.targetVertex.name, 'weight': e.weight}
            if Output.contains(data):
                print("Edge already exists: ({}, {}, {})".format(e.startVertex.name,e.targetVertex.name,e.weight))
            else:
                Output.insert(data)
    # @Source is a database containing data for vertices
    # @Output is a graph object where vertices will be created using data from the Source
    def downloadVertices(self, Output):
        vertexList = self.vertices.fetch_all_entries()
        for vertex in vertexList:
            Output.addVertex(vertex['name'])

class Item():
    def __init__(self, id):
        self.id
