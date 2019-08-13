from Modules.Toolkit.Graph.Graph import Graph
from Modules.SmartyPants.SmartyPants import SmartyPants

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


if __name__ == "__main__":   
    print("welcome")
    testBasicGraph()
    app = SmartyPants()
    app.addItem('shirt', VertexId=0, Name='Red Yellowstone T-Shirt')
    app.addItem('shirt', VertexId=2, Name='FBI Seattle T-Shirt')
    app.addItem('shirt', VertexId=3, Name='G-Eazy Concert T-Shirt')
    app.addItem('pants', VertexId=1, Name='Sweatpant Style Shorts')
    app.printCloset()


