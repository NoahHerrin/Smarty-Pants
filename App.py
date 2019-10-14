from Modules.Toolkit.Graph.Graph import Graph
from Modules.Closet.Closet import Closet
import random
import math
import re
## ------------------------------------------------------------------- ##
## function: testBasicGraph
## purpose: initializes a simple graph and run's dijkstra's algorithmn
##          to find the best path from vertex 'a' to vertex 'd'
## ------------------------------------------------------------------- ##

def testBasicGraph():
    graph = Graph()

    a = graph.addVertex()
    b = graph.addVertex()
    c = graph.addVertex()
    d = graph.addVertex()

    graph.addEdge(5, a, b)
    graph.addEdge(2, a, b)
    graph.addEdge(1, c, d)
    graph.addEdge(3, b, d)

    graph.printGraphInfo()

    graph.calculateShortestPath(a)
    print(graph.getShortestPathTo(d))

## ------------------------------------------------------------------- ##
## function: testBasicCloset
## purpose: initializes a Closet with several items and displays the 
##          contents of the closet
## ------------------------------------------------------------------- ##

def testBasicCloset():
    app = Closet()
    app.addItem('shirt', VertexId=0, Name='Red Yellowstone T-Shirt')
    app.addItem('shirt', VertexId=2, Name='FBI Seattle T-Shirt')
    app.addItem('shirt', VertexId=3, Name='G-Eazy Concert T-Shirt')
    app.addItem('pants', VertexId=1, Name='Sweatpant Style Shorts')
    app.printCloset()

## -------------------------------------------------------------------- ##
## function: testBasicInterface
## purpose: generates 'n' items and add's them to interface and checks that
##          that everything is working as it is supposed to
## parameters: app, n
## -------------------------------------------------------------------- ##

def testBasicInterface(app, n):
    color = ['red', 'yellow', 'blue', 'green','pink', 'turqoise', 'striped', 'dots', 'gucci']
    type = ['shoes', 'pants', 'shirt', 'layer']

    for i in range(n - 1):
        rand1 = math.floor(random.random() * len(color))
        rand2 = math.floor(random.random() * len(type))
        app.addItem("{} {}".format(color[rand1], type[rand2]), type[rand2])
    app.addItem("final Item", 'layer')


## ------------------------------------------------------------------ ##
## function: testOutfitGenerator
## purpose: generates a small wardrobe and generates an outfit
## ------------------------------------------------------------------ ##

def testOutfitGeneration():
    app = Interface()

    # # put together random wardrobe
    # a = app.addItem(name="Air Force 1", catagoryName='shoes')
    # b = app.addItem(name="Van's old skool", catagoryName='shoes')
    # c = app.addItem(name="Black skinny jeans", catagoryName='pants')
    # d = app.addItem(name="Sweatpant Shorts", catagoryName='pants')
    # f = app.addItem(name="National Park T-Shirt", catagoryName='shirt')
    # g = app.addItem(name='Motion Boardshop T-Shirt', catagoryName='shirt')
    
    testBasicInterface(app, 100)

    app.debugDS()
    # generate outfit
    outfit = app.getBestOutfit(0,99)

    # print out outfit combination
    for item in outfit:
        item.debugItem()
    return app
    # app.debugDS()


## --------------------------------------------------------------- ##
## function: TestEdgeCreation
## purpose: testing edge creation between item objects
## --------------------------------------------------------------- ##

def testEdgeCreation():
    app = Interface()
    
    # create items
    a = app.addItem(name="Air Force 1", catagoryName='shoes')
    b = app.addItem(name="Van's old skool", catagoryName='shoes')
    c = app.addItem(name="Black skinny jeans", catagoryName='pants')
    d = app.addItem(name="Sweatpant Shorts", catagoryName='pants')
    f = app.addItem(name="National Park T-Shirt", catagoryName='shirt')
    # g = app.addItem(name='Motion Boardshop T-Shirt', catagory='shirt')

    Graph = app.getGraph()
    Graph.addEdge(5, a, c)
    Graph.addEdge(5, a, d)
    Graph.addEdge(5, b, c)
    Graph.addEdge(5, b, d)
    Graph.addEdge(5, d, f)
    Graph.addEdge(5, c, f)
    
    app.debugDS()

    outfit = app.getBestOutfit(a, f)
    # print outfit
    for item in outfit:
        item.debugItem()


## --------------------------------------------------------------- ##
## function: testGraphSaving
## purpose: tests graph's ability to save data to a text file
## --------------------------------------------------------------- ##
def testGraphSaving():
    app = Interface()
    testBasicInterface(app, 10)
    file = open("Sample.txt", "w")
    app.saveAppData(file)
    app.debugDS()

## --------------------------------------------------------------- ##
## object: Interface
## purpose: A mechansim for synchronizing the Graph datastructure
##          and the Closet datastructure
## methods: 
## variables: __graph, __closet
## --------------------------------------------------------------- ##

class Interface(object):
    DEFAULT_EDGE_WEIGHT = 5
    def __init__(self):
        self.__graph = Graph()
        self.__closet = Closet()

    def getGraph(self):
        return self.__graph
    ## ---------------------------------------------------------- ##
    ## function: addItem
    ## purpose: creates a new item in both __graph and __closet
    ##          and necessary incoming and outgoing edges.
    ## parameters: name, catagoryName
    ## ---------------------------------------------------------- ##

    def addItem(self, name, catagoryName):
        # create vertex 
        id = self.__graph.addVertex()

        # create item 
        self.__closet.addItem(Name = name, Catagory = catagoryName, VertexId = id)

        # fetch catagory
        catagory = self.__closet.getCatagory(catagoryName)

        # incoming edges

        # get previous catagory
        previous = catagory.getPreviousCatagory()  
  
        # check if previous catagory exists
        if previous is not None:
            items = previous.getItems()
            if items is not None:
                # create incoming edges
                for item in items:
                    self.__graph.addEdge(math.floor(random.random() * 10), item.getVertexId(), id)

        # outgoing edges

        # fetch next catagory
        nextCat = catagory.getNextCatagory()
        if nextCat is not None:
            items = nextCat.getItems()
            if items is not None:
                # create outgoing edges
                for item in items:
                    self.__graph.addEdge(math.floor(random.random() * 10), id, item.getVertexId())

        return id

    ## ----------------------------------------------------------- ##
    ## function: getBestOutfit
    ## purpose: finds the best outfit combination composed of two items
    ## parameters: startVertex, endVertex
    ## returns: list of item objects
    ## ----------------------------------------------------------- ##
    
    def getBestOutfit(self, startVertex, endVertex):
        print("Finding Best Path\n\tStarting Vertex: {}\n\tEnding Vertex: {}".format(startVertex, endVertex))
        # run dijkstra's aglorithmn to find optimal path to all clothing items
        self.__graph.calculateShortestPath(startVertex)
        # find best path from startVertex to endVertex
        path = self.__graph.getShortestPathTo(endVertex)
        print("\tVertex Path: {}".format(path))
        outfit = []
        # convert vertexId's to Item objects
        for vertex in path:
            outfit.append(self.__closet.getItem(vertexId=vertex))
        return outfit

    ## --------------------------------------------------------------------- ##
    ## function: saveAppData
    ## purpose: Preserves app data by storing it at a destination
    ## parameters: destination
    ## notes: assume destination is a file with read/write permisions
    ##        saves in format
    ##        number of Vertices
    ##        origin of edge1, destination of edge1, weight of edge1
    ##        origin of edge2, destination of edge2, weight of edge2
    ##        ...
    ## future: allow for saving to both file and database
    ## --------------------------------------------------------------------- ##

    def saveAppData(self, destination):
        destination.write(self.__graph.getGraphInfo())
        print(self.__closet.getClosetData())

    ## --------------------------------------------------------------------- ##
    ## function: loadAppData
    ## purpose: to load previous Interface data from persistant storage
    ## parameters: graphSource, itemSource
    ## --------------------------------------------------------------------- ##

    def loadAppData(self, graphSource, itemSource):

        # first load graph
        fileContents = graphSource.read()
        data = fileContents.split('\n')
        if len(data) > 1:
            # load vertices
            numVertices = int(data[0])
            for i in range(numVertices):
                self.__graph.addVertex()
            # load edges
            for i in range(1,len(data) - 1):
                # parse file into weight, origin, destination
                edgeData = re.findall("\d{1,4}",data[i])
                self.__graph.addEdge(int(edgeData[0]), int(edgeData[1]), int(edgeData[2]))
        else:
            raise Exception('Unable to load app data')

        # second load graph

         
    def debugDS(self):
        self.__closet.printCloset()
        self.__graph.printGraphInfo()


if __name__ == "__main__":   
    print("Smarty Pants (beta)")
    app = testOutfitGeneration()
    # testGraphSaving()    



