import sys

class Vertex(object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize
    def __cmp__(self, otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)
    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority
    def printData(self):
        print("Vertex Data")
        print("Name: {}".format(self.name))
        print("Predecessor: {}".format(self.predecessor))
        print("Adjacencies List: ", end="")
        length = len(self.adjacenciesList)
        for idx in range(length):
            if idx is not length:
                print(self.adjacenciesList[idx].getInfo(), end=", ")
        print("\nMinimum Distance: {}".format(self.minDistance))
