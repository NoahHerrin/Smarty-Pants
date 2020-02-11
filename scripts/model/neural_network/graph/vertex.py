import sys

class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.visted = False
        self.predecessor = None 
        self.adjacent_verticies = []
        self.min_distance = sys.maxsize

    def get_predecessor(self):
        # confirm that path findng algorithmn has been applied
        if self.predecessor is None:
            raise Exception("Predecessor for vertex: {} does not exist, try running path findign algorithmn.".format(self.id))
        return self.predecessor
    
    def is_visited(self):
        return self.visted

    def set_visited(self, value):
        self.visited = value

    def get_adjacent_verticies(self):
        return self.adjacent_verticies

    def add_adjacent_vertex(self, other_vertex):
        return self.adjacent_verticies.append(other_vertex)