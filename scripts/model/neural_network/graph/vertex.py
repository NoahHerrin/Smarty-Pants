import sys
from typing import List

class Vertex(object):
    """ wrapper object for a vertex in a grath

        Wrapper object to store a vertex object's relations to other verticies along with it's locational
        relations to other verticies. 

    """
    def __init__(self, id):
        """accepts a unique integer as a parameter to use as an id."""

        self._id = id
        self._is_visited = False
        self._predecessor = None 
        self._adjacent_verticies = []
        self._min_distance = sys.maxsize

    def get_id(self):
        """returns the id of this vertex"""
        return self._id
        
    def get_predecessor(self):
        """return's the vertex precedding this vertex."""

        # if predecessor is null then algorithmn has not been correctly applied.
        if self._predecessor is None:
            raise Exception("Predecessor for vertex: {} does not exist, try running path findign algorithmn.".format(self._i_id))
        return self._predecessor
    
    def is_visited(self):
        """returns whether this graph has been visited already"""

        return self._visted

    def set_visited(self, value):
        """accepts a boolean parameter and will set the value of _is_visited accordingly"""

        self._is_visited = value

    def get_adjacent_verticies(self):
        """returns list of adjacent verticies"""

        return self._adjacent_verticies

    def add_adjacent_vertex(self, other_vertex):
        """adds vertex to list of adjacent verticies"""
        return self._adjacent_verticies.append(other_vertex)
        
    def __str__(self):
        """formats data stored by vertex to be displayed"""
        # add in single value variables
        retVal = "id: {}, visited: {}, predecessor: {} ".format(self._id, self._is_visited, self._predecessor)

        # add in adjacent vertecies
        adjacent_v = "(" # "(" +  map(lambda: v: "{}, ".format(v), self._iadjacent_verticies) + ")"

        for vertex, index in enumerate(self._adjacent_verticies):
            suffix = "" if index == len(self._adjacent_verticies) else ", "
            adjacent_v += str(vertex.id) + suffix
        adjacent_v += ")"
        # add min_distance
        retVal += "{}, min_distance: {}".format(adjacent_v, self._min_distance)

        return retVal
