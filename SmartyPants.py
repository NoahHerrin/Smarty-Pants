from Dijkstra.Graph import Graph
from Dijkstra.Edge import Edge
from Dijkstra.Vertex import Vertex
import DBConnector as DB


class Item(object):
    def __init__(self, id, name,  type):
        self.id = id
        self.namen = name
        self.type = type
        self.properties = {}
    def updateProperty(self, attribute, value):
        self.properties[attribute] = value
    def checkProperty(self, property, expected):
        if property in self.properties:
            if property[property] is expected:
                return True
        return False

class Closet(object):
    def __init__(self):
        self.closet = {
            'layer' : [],
            'shirt' : [],
            'shoes' : [],
            'pants' : []
        }
    def addItem(self, item):
        type = item.type
        if type in self.closet:
            self.closet[type].append(item)
            return True
        return False

class SmartyPants(object):
    def __init__(self):
        self.vertices = DB.connect("vertices", {'titles': ['name']})
        self.edges = DB.connect("edges", {'titles': ['weight','origin','destination']})
        self.closet = Closet()
        self.downloadGraph()
    def downloadGraph(self):
        self.graph = Graph()
        vertices = self.downloadVertices()
        edges = self.downloadEdges(self.graph)
    def uploadGraph(self):
        self.uploadVertices()
        self.uploadEdges()
    def uploadVertices(self):
        vertexList = self.graph.VertexList
        for v in vertexList:
            if self.vertices.contains({'name':v.name}):
                print("Vertex {} already exists".format(v.name))
            else:
                self.vertices.insert({'name': v.name})
    # def addItem(self, id, itemName, type):

    # @Output specifies where the edges will be uploaded to
    # @Graph specicifies the graph whose edges will be uploaded
    def downloadEdges(self, Output):
        edgeList = self.edges.fetch_all_entries()
        for edge in edgeList:
            Output.addEdge(edge['weight'], edge['origin'], edge['destination'])

    def uploadEdges(self):
        edgeList = self.graph.EdgeList
        for e in edgeList:
            data = {'origin': e.startVertex.name, 'destination': e.targetVertex.name, 'weight': e.weight}
            if self.edges.contains(data):
                print("Edge already exists: ({}, {}, {})".format(e.startVertex.name,e.targetVertex.name,e.weight))
            else:
                self.edges.insert(data)
    # @Source is a database containing data for vertices
    # @Output is a graph object where vertices will be created using data from the Source
    def downloadVertices(self):
        vertexList = self.vertices.fetch_all_entries()
        for vertex in vertexList:
            self.graph.addVertex(vertex['name'])
    def createMultipleOutgoingEdges(self,origin, destinations, weight):
        if len(destinations) is 0:
            return
        for other in destinations:
            self.graph.addEdge(weight, origin, other.id)
    def createMultipleIncomingEdges(self,origins, destination, weight):
        if len(origins) is 0:
            return
        for other in origins:
            self.graph.addEdge(weight, other, destination)

    def addItem(self, name, type):
        # create vertex for item
        # create item for item
        # create edges for vertex
        vertex_id = self.graph.addVertex()
        item = Item(vertex_id, name,  type)
        self.closet.addItem(item)
        vertex = self.graph.getVertex(vertex_id)
        # THERE HAS TO BE A BETTER WAY BUT SHOES WOULD NOT HAVE A PREVIOUS AND LAYER WOULD NOT HAVE A NEXT
        #
        if type.lower() == "shirt":
            # create edges from all pants to this shirt
            # create edges from this shirt to all layers
            self.createMultipleOutgoingEdges(vertex_id, self.closet.closet['layer'], 5)
            self.createMultipleIncomingEdges(self.closet.closet['pants'], vertex_id, 5)
        elif type.lower() == "layer":
            self.createMultipleIncomingEdges(self.closet.closet['shirt'], vertex_id, 5)
        elif type.lower() == "pants":

            self.createMultipleOutgoingEdges(vertex_id, self.closet.closet['shirt'], 5)
            self.createMultipleIncomingEdges(self.closet.closet['shoes'], vertex_id, 5)
        elif type.lower() == "shoes":
            self.createMultipleOutgoingEdges(vertex_id, self.closet.closet['pants'], 5)
