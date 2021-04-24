import networkx as nx
import sys

G = nx.Graph()

with open("instances/2-FullIns_4.col", "r") as f:
    
    for i in range(6):
        f.readline()
    
    infoGraph = f.readline()
    n_vertices = int(infoGraph.split()[2])
    n_edges = int(infoGraph.split()[3])
    
    for i in range(n_edges):
        edgeString = f.readline()
        G.add_edge(int(edgeString.split()[1]), int(edgeString.split()[2]))
    
    print(list(G[1].keys()))