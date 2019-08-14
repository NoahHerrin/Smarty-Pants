from Modules.Toolkit.Graph.Graph import Graph
from Modules.Closet.Closet import Closet

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

    ## ---------------------------------------------------------- ##
    ## function: addItem
    ## purpose: creates a new item in both __graph and __closet
    ##          and necessary incoming and outgoing edges.
    ## parameters: name
    ## ---------------------------------------------------------- ##

    def addItem(self, name, catagory):
        # create vertex ✓
        id = self.__graph.addVertex()

        # create item ✓
        self.__closet.addItem(Name = name, Catagory = catagory, VertexId = id)

        # create incoming edges
        if self.__closet.getCatagory(catagory).getPreviousCatagory() is not None:
            incoming = self.__closet.getCatagory(catagory).getPreviousCatagory().getItems()
            if incoming is not None:
                for vertex in incoming:
                    # create edge from vertex to new vertex
                    self.__graph.addEdge(self.DEFAULT_EDGE_WEIGHT, vertex.getVertexId(), id)

        # create outgoing edges
        if self.__closet.getCatagory(catagory).getNextCatagory() is not None:
            outgoing = self.__closet.getCatagory(catagory).getNextCatagory().getItems()
            if outgoing is not None:
                for vertex in outgoing:
                    # create edge from new vertex to vertex
                    self.__graph.addEdge(self.DEFAULT_EDGE_WEIGHT, id, vertex.getVertexId())
                
            return id

    def debugDS(self):
        self.__closet.printCloset()
        self.__graph.printGraphInfo()

        
if __name__ == "__main__":   
    print("starting up application")
    app = Interface()
    app.addItem('Yellow T-Shirt', 'shirt')
    app.addItem('Blue Shirt', 'shirt')
    app.addItem('Black-Grey Skinny Jeans', 'pants')
    app.addItem('White Air Jordan 1 ', 'shoes')
    app.addItem('Hoodie', 'layer')
    app.addItem('Denim Jacket', 'layer')
    app.debugDS()



