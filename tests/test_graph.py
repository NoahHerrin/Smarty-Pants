from scripts.model.neural_network.graph.vertex import Vertex
from scripts.model.neural_network.graph.edge import Edge
from scripts.model.neural_network.graph.graph import Graph
import unittest

class Test_Graph(unittest.TestCase):
    def test_add_get_remove_vertex(self):
        """Runs tests on 
                Graph.add_vertex
                Graph.get_vertex
                Graph.remove_vertex

            Edge Cases
                1) test for incorrect parameter types for
                   get_vertex and remove_vertex.
                2) Test with normal inputs
                3) test remove_vertex and get_vertex
                   with non existant vertex id's
            Note:
                This test is only concerned about
                remove_vertex removing the vertex
                testing for remove_vertex removing 
                the vertex along with all it's 
                edges will be in a different test.
        """
        g = Graph()

        # CASE 1
        illegal_params = [False, None, "1", "Vertex"]
        
        # test add_vertex
        for param in illegal_params:
            self.assertRaises(TypeError, g.get_vertex)
        # test remove_vertex    
        for param in illegal_params:
            self.assertRaises(TypeError, g.remove_vertex)

        # CASE 2

        # test add_vertex and get_vertex
        # add verticies to graph
        # check if get_vertex will correctly find the vertex each time
        for id in range(10):
            new_id = g.add_vertex()
            self.assertEqual(id, g.get_vertex(new_id).get_id())
        
        # test remove_vertex
        # remove all verticies first
        for id in range(10):
            self.assertEqual(g.remove_vertex(0).get_id(), id) 
        
        # then try to remove them all again, this should throw an exception
        for id in range(10):
            self.assertRaises(ValueError, g.remove_vertex, id)
        
        

        pass
    def test_get_index_of_vertex(self):
        """Runs test on 
                Graph.get_index_of_vertex
        """
        pass
    def test_get_add_edge(self):
        """Runs tests on 
                Graph.get_edge
                Graph.add_edge_with_id
                Graph.add_edge_with_verticies
        """
        pass
    def test_remove_edge(self):
        """Runs tests on 
                Graph.remove_edge
        """
        pass
    def test_contains_edge(self):
        """Runs tests on 
                Graph.contains_edge
        """
        pass
    def test_contains_vertex(self):
        """Runs tests on
                Graph.contains_vertex
        """

