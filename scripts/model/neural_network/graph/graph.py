from scripts.model.neural_network.graph.vertex import Vertex

class Graph(object):
    """Graph datastructure
        
        A datastructure used to represent verticies and their relations(edges)
        to other verticies
    """
    def __init__(self):
        """Creates a new graph object"""
        self.next_id = 0 # used to assign a unique id to each node
        self.verticies = [] # automatically sorted in order id = index
        self.edges = [] # required operations add, search, delete (importance in that order), sort by origin int
    
    def add_vertex(self):
        """creates new vertex and returns the id of the new vertex"""

        self.verticies.append(Vertex(next_id))
        self.next_id += 1
        return self.next_id - 1
        
    def get_vertex(self, id):
        """Use binary search to find a vertex in the list and return it"""
        if not id > len(self.verticies) and len(self.verticies) is not 0:
            index = self.get_index_of_vertex(id)
            if index is not -1:
                return self.verticies[index]
            else:
                raise Exception("Invalid id: {}".format(id))

        else:
            raise Exception("Attempted to access an invalid vertex with id = {}".format(id))

    def get_index_of_vertex(self, id):
        """Use binary search to find a vertex. 
        Args:
            id: int
            the id of the vertex to be found
        
        Return:
            int >= 0 if vertex exists
            int = -1 if vertex does not exist"""

        i = int(len(self.verticies) / 2)

        while i < (len(self.verticies) - 1) and i > 0:

            if self.verticies[i].get_id() == id:
                return self.verticies[i]

            elif self.verticies[i].get_id() < id:
                i = int(i / 2)
            else:
                i = i + int(i/2)
        return -1

    def remove_vertex(self, id):
        """Removes vertex with provided id from graph. All edges using the vertex will be deleted also"""
        index = self.get_index_of_vertex(id)
        
        if index is -1:
            raise Exception("Vertex with id {} does not exist.".format(id))

        self.verticies.pop(index)


        
    def add_edge_with_id(self, id, destination, weight):
        """ adds an edge using the int ids of the verticies you want to add"""
        

        pass
    def add_edge_with_verticies(self, origin, destination, weight):
        """ returns the edge with verticies origin and destination """
        pass
    def get_edge(self, origin: int, destination: int):
        """use integer id's to find the appropriate edge"""
        pass
    def remove_edge(self, origin: int, destination: int):
        pass
    def contains_edge(self, origin: int, destination: int):
        pass