from Toolkit.Graph.Graph import Graph

if __name__ == "__main__":   
    print("welcome")
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