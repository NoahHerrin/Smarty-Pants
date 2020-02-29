import unittest
from scripts.model.neural_network.graph.vertex import Vertex

class TestVertex(unittest.TestCase):

    def test_initialize(self):
        """Tests whether vertex will only allow the correct parameters to be used as an id"""
        illegal_params = ["1", "Word", False, True]

        for param in illegal_params:
            self.assertRaises(TypeError, Vertex, param)
        
        legal_params = [1, 10, 100]
        for param in legal_params:
            try:
                Vertex(param)
            except TypeError:
                self.fail("TypeError for parameter: {}".format(param))
             
    def test_equals(self):
        """Tests equals overrides
        Tests
        -----
        InputType
            Tests whether function will throw an error if an object of an
            incompatible type is passed as a parameter
        CorrectResults
            Tests comparison of verticies
        """

        # Test input types
        illegal_params = ["1", True, None]
        vertex = Vertex(1)

        for param in illegal_params:
            self.assertRaises(TypeError, vertex.__eq__, param)
        
        # Test comparison
        different_vertex = Vertex(2)
        self.assertEqual(vertex.__eq__(different_vertex), False)
        self.assertEqual(vertex.__eq__(vertex), True)


    def test_get_id(self):
        """Tests get_id function

        Tests
        -----
        Correct Id
            Tests whether the returned id is correct

        """
        for id in range(10):
            vertex = Vertex(id)
            self.assertEqual(vertex.get_id(), id)
        

    def test_adjacencies(self):
        """Test get_adjacent_verticies and add_adjacent_vertex

        Tests
        -----
        TestAddAdjacentVertex
            Tests whether adding an adjacent vertex works correctly
        TestGetAdjacentVerticies
            Tests whether program correctly gets adjacetn verticies
        """

        # test without any adjacent verticies
        vertex = Vertex(0)
        self.assertEqual(vertex.get_adjacent_verticies(), [])

        other_vertex = Vertex(1)
        vertex.add_adjacent_vertex(other_vertex)
        self.assertEqual(vertex.get_adjacent_verticies(),[other_vertex])

        # Stress test, test that adjacent 
        for i in range(100):
            other = Vertex(i)
            vertex.add_adjacent_vertex(other)
            adjacencies = vertex.get_adjacent_verticies()
            self.assertEqual(other in adjacencies, True)


        

    def test_visited(self):
        """Test is_visited and set_visited
        
        Tests
        -----
        TestUnvisited
            Tests whether visited will work correctly when unvisted
        TestVisited
            Tests whether visited will work correctly when visited
        """

        vertex = Vertex(0)
        self.assertFalse(vertex.is_visited())
        
        vertex.set_visited(True)
        self.assertTrue(vertex.is_visited())
        
        vertex.set_visited(False)
        self.assertFalse(vertex.is_visited())
        

    def test_predecessor(self):
        """Tests get_predecessor and set_predecessor

        Tests
        -----
        Test get_predecessor
            Test without any predecessors

        Test set_predecessor
            Test with predecessors being added

        """
        vertex = Vertex(0)
        self.assertRaises(AttributeError, vertex.get_predecessor)
        
        predecessor = Vertex(1)
        vertex.set_predecessor(predecessor)
        self.assertEqual(vertex.get_predecessor(),predecessor)

        new_predecessor = Vertex(2)
        vertex.set_predecessor(new_predecessor)
        self.assertEqual(vertex.get_predecessor(), new_predecessor)
        pass

