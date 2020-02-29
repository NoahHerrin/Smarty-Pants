import sys
sys.path.append("..")

from scripts.model.neural_network.graph.vertex import Vertex

def vertex_test():
    v = Vertex(1)
    print(v)