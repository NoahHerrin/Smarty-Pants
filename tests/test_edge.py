from scripts.model.neural_network.graph.edge import Edge
from scripts.model.neural_network.graph.vertex import Vertex
import unittest

class TestEdge(unittest.TestCase):

    def test_constructor(self):
        """test constructor for Edge"""
        illegal_verticies = [1, True, "Who knows"]
        illegal_weights = [True, "Who Knows"]
        
        # cases 1: incorrect parameter data type for vertecies
        vertex = Vertex(0)
        for illegal in illegal_verticies:
            self.assertRaises(TypeError, Edge, vertex, illegal, 5)

        # case 2: incorrect weight type
        vertex2 = Vertex(0)
        for illegal in illegal_weights:
            self.assertRaises(TypeError, Edge, vertex, vertex2, illegal)

        # case 3: origin == destination, can't have a path leading to itself
        self.assertRaises(ValueError, Edge, vertex, vertex2, 10)

    def test_contains_vertex(self):
        """test contains_vertex function from edge"""
        illegal_params = [1, False, "Not a vertex"]
        
        vertex1 = Vertex(0)
        vertex2 = Vertex(1)
        vertex3 = Vertex(2)
        test_edge = Edge(vertex1, vertex2, 1)

        # test that contains_vertex rejects all invalid datatypes
        for param in illegal_params:
            self.assertRaises(TypeError, test_edge.contains_vertex, param)
        
        # test for vertex that IS in the edge
        self.assertEqual(test_edge.contains_vertex(vertex1), True)

        # test that a vertex IS NOT in the edge
        self.assertEqual(test_edge.contains_vertex(vertex3), False)

    def test_modify_weight(self):
        """performs tests on modify_weight"""

        vertex1 = Vertex(0)
        vertex2 = Vertex(1)
        test_edge = Edge(vertex1, vertex2, 1)

        # case 1: test for invalid parameter types
        illegal_params = [None, True, "10", "N"]
        for param in illegal_params:
            self.assertRaises(TypeError, test_edge.modify_weight, illegal_params)
        
        # case 2: test addition
        test_edge.modify_weight(5)
        self.assertEqual(test_edge.get_weight(), 6)

        # case 3: test subtraction
        test_edge.modify_weight(-1)
        self.assertEqual(test_edge.get_weight(), 5)

    def test_equivalence(self):
        """test __eq__ function for Edge"""
        
        vertex = Vertex(0)

        # case 1: test typing
        illegal_params = [True, "Not a vertex", None]
        for param in illegal_params:
            self.assertRaises(TypeError, vertex.__eq__, param)

        # case 2: test false comparison
        other = Vertex(1)
        self.assertEqual(vertex.__eq__(other), False)
        # case 3: test true comparison
        self.assertEqual(vertex.__eq__(vertex), True)