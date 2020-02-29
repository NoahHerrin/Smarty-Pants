class Edge(object):
    """wrapper object of containing edge information in a graph
    
        Contains an origin and destination vertex with a weight representing the
        cost of moving from the origin to the destination.
    """
    def __init__(self, origin, destination, weight):
        self._origin = origin
        self._destination = destination
        self._weight = weight
    
    def contains_vertex(self, vertex):
        """accepts a vertex and returns whether the vertex is used in this edge"""

        return vertex.id == self._origin or self.id == self._destination

    def get_origin(self):  
        """returns the origin vertex of this edge"""
        return self._origin

    def get_destination(self):
        """returns the destination vertex of the edge"""
        return self._destination

    def get_weight(self):
        """returns the weight of the edge"""
        return self._weight

    def modify_weight(self, delta_weight):
        """ accepts a numerical value and adds it to the current weight
            example.
            modify_weight(-x) -> _weight - x
            modify_weight(x)  -> _weight + x
        """
        self._weight += delta_weight
