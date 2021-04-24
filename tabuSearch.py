import networkx as nx
import sys

testMode = len(sys.argv) == 2 and sys.argv[1] == "test"

if (len(sys.argv) != 3 and not testMode):
    print("a chamada ao programa deve ser: \"python tabuSearch.py <seed> <instancia de grafo>\"")

if (testMode):
    seed = 0
    instanceFileName = "instances/2-FullIns_4.col"
else:
    seed = int(sys.argv[1])
    instanceFileName = sys.argv[2]


G = nx.Graph()

with open(instanceFileName, "r") as f:
    
    for i in range(6):
        f.readline()
    
    infoGraph = f.readline()
    n_vertices = int(infoGraph.split()[2])
    n_edges = int(infoGraph.split()[3])
    
    for i in range(n_edges):
        edgeString = f.readline()
        G.add_edge(int(edgeString.split()[1]), int(edgeString.split()[2]))
    
    print(list(G[1].keys()))