import SmartyPants as sp
from Dijkstra.Graph import Graph

app = sp.SmartyPants()
g = app.downloadGraph()
print('graph data downloaded')
g.printGraphInfo()
