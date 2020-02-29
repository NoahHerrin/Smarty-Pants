import sys
from typing import List


class Vertex(object):
    """ wrapper object for a vertex in a grath

        Wrapper object to store a vertex object's relations to other verticies along with it's locational
        relations to other verticies. 
        
        Attributes
        ----------
        _id: int
            a unique integer id for this vertex
        _is_visited: bool
            represents whether a vertex has been visited in a traversal
        _predecessor: Vertex
            The vertex that preceeds this vertex in a path 
        _adjacent_verticies: List[Vertex]
            A list of all verticies connected to this vertex
        _min_distance: int
            this minimum distance from the origin of a path  

        Example
        -------
        >> from vertex import Vertex
        >>
        >> vertex = Vertex(0)
        

    """
    # Complete Tested
    def __init__(self, id):
        """accepts a unique integer as a parameter to use as an id.

        Intializes an instance of Vertex using a unique integer parameter. 
        The id will be used to identify the specific instance when the 
        Vertex is apart of a larger datastructure like a graph

        Parameter
        ---------
        id: int
            a unique id for a vertex

        Raises
        ------
        TypeError
            Raised if parameter id is not datatype int

        """
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError("Invalid type for parameter id: {}".format(type(id)))

        self._id = id
        self._is_visited = False
        self._predecessor = None 
        self._adjacent_verticies = []
        self._min_distance = sys.maxsize

    # Complete Untested
    def get_id(self):
        """returns the id of this vertex

        Example
        -------
        >> from vertex import Vertex
        >>
        >> vertex = Vertex(0)
        >> vertex.get_id()
        0
        """
        return self._id

    # Complete Untested
    def set_predecessor(self, other_vertex):
        """Sets the predecessor of vertex to other_vertex

        Parameter
        ---------
        other_vertex: Vertex
            the vertex that comes before it on some path

        Raises
        ------
        TypeError
            Raised if other_vertex is not an instance of Vertex
        
        Example
        -------
        >> from vertex import Vertex
        >>
        >> vertex1 = Vertex(0)
        >> vertex2 = Vertex(1)
        >> vertex1.set_predecessor(vertex2)
        >> vertex1.get_predecessor()
        vertex2
        """
        if not isinstance(other_vertex, Vertex):
            raise TypeError("Invalid type for parameter other_vertex: {}".format(type(other_vertex)))
        else:
            self._predecessor = other_vertex
    
    # Complete Untested
    def get_predecessor(self):
        """return's the vertex precedding this vertex.
        
        Return
        ------
        Vertex
            The instance of vertex that preceeds this Vertex in a path

        Raises 
        AttributeError
            Raised when predecessor hasn't been set

        Example
        -------
        >> from vertex import Vertex
        >>
        >> vertex1 = Vertex(0)
        >> vertex2 = Vertex(1)
        >> vertex1.set_predecessor(vertex2)
        >> vertex1.get_predecessor()
        vertex2
        """

        # if predecessor is null then algorithmn has not been correctly applied.
        if self._predecessor is None:
            raise AttributeError("Predecessor for vertex: {} does not exist.".format(self._id))

        return self._predecessor
    
    # Complete Untested 
    def is_visited(self):
        """returns whether this graph has been visited already
        
        Returns
        -------
        bool
            True if vertex has been visited, false otherwise
        
        Example
        -------
        >> from vertex import Vertex
        >>
        >> vertex1 = Vertex(0)
        >> vertex1.is_visited()
        False
        """

        return self._is_visited
    
    # Complete Untested 
    def set_visited(self, value):
        """accepts a boolean parameter and will set the value of _is_visited accordingly
        
        Parameter:
        value: bool
            the value of visited that visited will be set to
        
        Return:
        bool
            the value of visited after the change has been made

        Raises:
        TypeError
            Error is raised if value is not of type bool
        
        Example
        -------
        >> from vertex import Vertex
        >>
        >> vertex1 = Vertex(0)
        >> vertex1.is_visited()
        False
        >> vertex2.set_visited(True)
        >> vertex2.is_visited()
        True

        """
        if not isinstance(value, bool):
            raise TypeError("Invalid type for arguement value: {}".format(type(value)))

        self._is_visited = value
        return self.is_visited

    # Complete Untested 
    def get_adjacent_verticies(self):
        """returns list of adjacent verticies
        
        Return
        ------
        List[Vertex]
            All the verticies that are connected to this vertex
            
        Example
        -------
        >> from vertex import Vertex
        >>
        >> vertex1 = Vertex(0)
        >> vertex1.get_adjacent_verticies()
        []
        """

        return self._adjacent_verticies

    # Complete Untested 
    def add_adjacent_vertex(self, other_vertex):
        """adds an vertex to the list of adjacent verticies
        
        Parameter
        ---------
        other_vertex: Vertex
            A vertex to be added to the list of adjacent verticies

        Example
        -------
        >> from vertex import Vertex
        >>
        >> vertex1 = Vertex(0)
        >> vertex1.get_adjacent_verticies()
        []
        >> vertex2 = Vertex(1)
        >> vertex1.add_adjacent_vertex(vertex2)
        >> vertex1.get_adjacent_verticies()
        [vertex2]
        
        Raises
        ------
        TypeError
            Raised when other_vertex is not an instance of Vertex
        """
        if not isinstance(other_vertex, Vertex):
            raise TypeError("Invalid type for parameter other_vertex: {}".format(type(other_vertex)))
        return self._adjacent_verticies.append(other_vertex)
        
    # Complete Untested     
    def __str__(self):
        """formats data stored by vertex to be displayed
        
        Returns
        -------
        str
            returns formatted vertex of vertex of the form
            (id: ..., visited: ..., predecessor: ..., number of edges: ..., min_distance: ...) """
        # add in single value variables
        template = "(id: {}, visited: {}, predecessor: {}, number of edges: {}, min_distance: {} )"
        predecessor = None if self.get_predecessor() is None else self.get_predecessor().get_id()
        return template.format(self._id, self._is_visited, predecessor, len(self.get_adjacent_verticies), self._min_distance)

    # Incomplete Untested
    def __eq__(self, other):
        """checks equivalence with another vertex

        Parameters
        ----------
        other: Vertex
            The vertex to compared to this vertex
        
        Returns
        -------
        bool
            True if verticies are equivalent, False otherwise

        Raises
        ------
        TypeError
            Raised if other is not an instance of Vertex
        
        """
        if not isinstance(other, Vertex):
            raise TypeError("Invalid parameter, type of other is {}, it should be Vertex".format(type(other)))
        return other.get_id() == self.get_id()
