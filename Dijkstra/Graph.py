from Dijkstra.Vertex import Vertex
from Dijkstra.Edge import Edge
from Dijkstra.Algorithm import Algorithm
import heapq
import sys

class Graph(object):
    def __init__(self):
        self.VertexList = []
        self.VertexIndicies = {}
        self.EdgeList = []
    def addVertex(self, vertexName):
        self.VertexIndicies[vertexName] = len(self.VertexList)
        self.VertexList.append(Vertex(vertexName))
    def addEdge(self, weight, originName, destinationName):
        # add check for duplicate edges from a single node (e.g A -5-> B and A -4-> B)
        # print(self.VertexIndicies[originName])
        origin = self.VertexList[self.VertexIndicies[originName]]
        destination = self.VertexList[self.VertexIndicies[destinationName]]
        edge = Edge(weight, origin, destination)
        origin.adjacenciesList.append(edge)
        self.EdgeList.append(edge)
    def calculateShortestPath(self, startVertex):
        vertexList = self.VertexList
        queue = []
        startVertex.minDistance = 0
        heapq.heappush(queue,startVertex)

        while len(queue) > 0:
            actualVertex = heapq.heappop(queue)
            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue,v)

    def getShortestPathTo(self, targetVertex):
        print("Shorest path to target is: ", targetVertex.minDistance)
        node = targetVertex
        path = []
        while node is not None:
            path.append(node.name)
            node = node.predecessor

        for i in range(len(path) - 1, 0, -1):
            print("{} -> ".format(path[i]),end="")
        print(targetVertex.name)
    def getVertex(self, VertexName):
        return self.VertexList[self.VertexIndicies[VertexName]]
    def getVertexWithLowestDistance(self, VertexSet):
        # NOT FUNCTIONAL WILL ALWAYS RETURN ORIGIN VERTEX #
        min = sys.maxsize
        vertex = None
        for v in VertexSet:
            if v.minDistance < min:
                min = v.minDistance
                vertex = v
        return vertex

    # print out list of nodes followed by details about all edges in the graph
    def printGraphInfo(self):
        print("Graph Info")
        print("Vertices: (", end="")
        length = len(self.VertexList)
        for i in range(length):
            print(self.VertexList[i].name, end="")
            if i is not (length - 1): print(", ",end="")

        print(")")

        print("Edges: ([origin], [destination], [weight])")
        for e in self.EdgeList:
            print("({}, {}, {})".format(e.startVertex.name, e.targetVertex.name, e.weight))
        print("")
