from scripts.model.neural_network.graph.vertex import Vertex
import math
class Graph(object):
    """Graph datastructure
        
        A datastructure used to represent verticies and their relations(edges)
        to other verticies
    """
    # Complete Untested 
    def __init__(self):
        """Creates a new graph object"""
        self.next_id = 0 # used to assign a unique id to each node
        self.verticies = [] # automatically sorted in order id = index
        self.edges = [] # required operations add, search, delete (importance in that order), sort by origin int
    
    # Complete Untested 
    def add_vertex(self):
        """creates new vertex and returns the id of the new vertex"""

        self.verticies.append(Vertex(self.next_id))
        self.next_id += 1
        return self.next_id - 1
    
    # Complete Untested     
    def get_vertex(self, id):
        """Use binary search to find a vertex in the list and return it"""
        # test for invalid parameter types
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError("Invalid parameter. id is type {}, should be int".format(type(id)))
        
        # test for out of bounds indecies
        if id >= len(self.verticies) and id < 0:
            raise ValueError("Invalid parameter, id must be greater than -1 and less than the number of verticies.")
        elif len(self.verticies) == 0:
            raise AttributeError("There are no verticies in the graph, try adding a vertex to the graph.")
        else:
            if len(self.verticies) == 1:
                if id == 0:
                    return self.verticies[0]
            else:    
                index = self.get_index_of_vertex(id)
                if index is not -1:
                    return self.verticies[index]
                else:
                    raise ValueError("Invalid id: {}".format(id))

    # Complete Untested 
    def binary_vertex_search(self, l, r, target):
        """Performs Binary Search on the list of verticies"""
        if r >= l:
            mid = l + int(round(((r - 1)/2), 0))
            if self.verticies[mid].get_id() == target:
                return self.verticies[mid]
            elif self.verticies[mid].get_id() > target:
                self.binary_vertex_search(l, mid - 1, target)
            else:
                self.binary_vertex_search(mid + 1, r, target)
        else:
            return -1

    def get_index_of_vertex(self, index):
        """"helper function for binary_vertex_search"""

        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("Invalid Parameter, index is type {}, should be int.".format(type(index)))
        
        return self.binary_vertex_search(0, len(self.verticies) - 1, index)
    
    # Complete Untested 
    def remove_vertex(self, id):
        """Removes vertex with provided id from graph. All edges using the vertex will be deleted also"""
        index = self.get_index_of_vertex(id)
        
        if index is -1:
            raise ValueError("Vertex with id {} does not exist.".format(id))

        return self.verticies.pop(index)


    # Incomplete Untested     
    def add_edge_with_id(self, id, destination, weight):
        """ adds an edge using the int ids of the verticies you want to add"""
        

        pass
    # Complete Untested 
    def add_edge_with_verticies(self, origin, destination, weight):
        """ returns the edge with verticies origin and destination """
        pass

    # Incomplete Untested
    def get_edge(self, origin, destination):
        """use integer id's to find the appropriate edge"""
        pass
    
    # Incomplete Untested
    def remove_edge(self, origin, destination):
        pass
    
    # Incomplete Untested
    def contains_edge(self, origin, destination):
        pass

    def contains_vertex(self, vertex):
        pass