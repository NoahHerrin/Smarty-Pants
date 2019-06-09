
class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
    def getInfo(self):
        return "({}, {}, {})".format(self.startVertex.name, self.targetVertex.name, self.weight)
