from Modules.Toolkit.Graph.Graph import Graph


# creates a simple graph and finds the shortest path from vertex a to vertex d
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

