from scripts.model.neural_network.graph.vertex import Vertex
class Edge(object):
    """wrapper object of containing edge information in a graph
    
        Contains an origin and destination vertex with a weight representing the
        cost of moving from the origin to the destination.
        Attributes
        ----------
        origin: Vertex
            vertex of the origin of the edge
        destination: Vertex
            vertex of the destination of the edge
        weight: int or float
            the weight or cost of traveling along this edge
            
        Example
        -------
        >> from vertex import Vertex
        >> from edge import Edge
        >>
        >> origin = Vertex(0)
        >> destination = Vertex(1)
        >> weight = 10
        >> edge = Edge(origin, destination, weight)

    """
    # Complete Untested 
    def __init__(self, origin, destination, weight):
        self._origin = origin
        self._destination = destination
        self._weight = weight
    
    # Complete Untested 
    def contains_vertex(self, vertex):
        """accepts a vertex and returns whether the vertex is used in this edge
        
        Parameter
        ---------
        vertex: Vertex
            an instance of vertex, that may be an origin or destination of this edge
        
        Return
        ------
            bool
                True if vertex is origin or destination, False otherwise

        Raises
        ------
        TypeError
            raises TypeError exception if parameter vertex is not an instance of Vertex
        
        Example
        -------
        >> from vertex import Vertex
        >> from edge import Edge
        >>
        >> origin = Vertex(0)
        >> destination = Vertex(1)
        >> weight = 10
        >> edge = Edge(origin, destination, weight)
        >>
        >> vertex = Vertex(2)
        >> edge.contains_vertex(vertex)
        False
        >> vertex = origin
        >> edge.contains_vertex(vertex)
        True
        """
        if not isinstance(vertex, Vertex):
            raise TypeError("Invalid type of parameter vertex: {}".format(type(vertex)))
        return vertex.id == self._origin or self.id == self._destination

    # Complete Untested 
    def get_origin(self):  
        """returns the origin vertex of this edge
        
        Return
        ------
        Vertex
            returns the instance of vertex being used as the origin of this edge
        
        Example
        -------
        >> from vertex import Vertex
        >> from edge import Edge
        >>
        >> origin = Vertex(0)
        >> destination = Vertex(1)
        >> weight = 10
        >> edge = Edge(origin, destination, weight)
        >>
        >> edge.get_origin()
        (origin id, origin is visited, origin predecessor, origin number of edges, origin min distance)
        """
        return self._origin
    
    # Complete Untested 
    def get_destination(self):
        """returns the destination vertex of this instance of edge
        
        Return
        ------
        Vertex
            returns the instance of vertex being used as the destination of this edge
        
        Example
        -------
        >> from vertex import Vertex
        >> from edge import Edge
        >>
        >> origin = Vertex(0)
        >> destination = Vertex(1)
        >> weight = 10
        >> edge = Edge(origin, destination, weight)
        >>
        >> edge.get_destination()
        (destination id, destination is visited, destination predecessor, destination number of edges, destination min distance)"""
        return self._destination
    
    # Complete Untested 
    def get_weight(self):
        """returns the weight of instance of edge
        Return
        ------
        float or int
            the current weight for this edge

        Example
        -------
        >> from vertex import Vertex
        >> from edge import Edge
        >>
        >> origin = Vertex(0)
        >> destination = Vertex(1)
        >> weight = 10
        >> edge = Edge(origin, destination, weight)
        >>
        >> edge.get_weight()
        weight

        """
        return self._weight
    
    # Complete Untested 
    def modify_weight(self, delta_weight):
        """ accepts a numerical value and adds it to the current weight

        Parameter
        ---------
        delta_weight: int or float (numerical types only)
            The the changen in weight for this instance of edge

        Returns
        -------
        numerical type
            the weight of the edge after the modification has been made

        Example
        -------
        >> from vertex import Vertex
        >> from edge import Edge
        >>
        >> origin = Vertex(0)
        >> destination = Vertex(1)
        >> weight = 10
        >> edge = Edge(origin, destination, weight)
        >>
        >> edge.get_weight()
        weight
        >> edge.modify_weight(5)
        weight + 5
        >> edge.modify_weight(-5)
        weight

        Raises
        ------
        TypeError
            raises exception if delta_weight was not a numerical type

        """
        if isinstance(delta_weight, int) or isinstance(delta_weight, float):
            self._weight += delta_weight
            return self.get_weight()
        else:
            raise TypeError("Invalid type for delta_weight parameter: {}".format(type(delta_weight)))
    
    # Complete Untested 
    def __eq__(self, obj):
        """Overrides equals operation to compare two instances of edge

            Parameters
            ----------
            obj: Edge
                an instance of edge to be checked against this current instance for equivalence.

            Returns
            ------- 
            bool
                True if edges are the same instance, otherwise False

            Raises
            ------
            TypeError:
                raised if type of object is not an edge

        """
        if isinstance(obj,Edge):
            return obj.get_origin() == self.get_origin() and obj.get_destination() == self.get_destination()
        else:
            raise TypeError("Invalid parameter type for obj: {}".format(type(obj)))

