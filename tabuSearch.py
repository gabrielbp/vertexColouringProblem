import networkx as nx
import sys
import matplotlib.pyplot as plt
import random
import copy
import datetime
from math import floor

testMode = len(sys.argv) == 2 and sys.argv[1] == "test"

if (len(sys.argv) != 3 and not testMode):
    print("a chamada ao programa deve ser: \"python tabuSearch.py <seed> <instancia de grafo>\"")

if (testMode):
    seed = 0
    instanceFileName = "instances/2-FullIns_3.col"
else:
    seed = int(sys.argv[1])
    instanceFileName = sys.argv[2]

random.seed(a=seed)


def generateNeighbour(graph, coloring, tabuQueue):
    n_nodes = graph.number_of_nodes()
    random_node = random.randint(0, n_nodes-1)

    color_space = set(range(len(coloring)))
    #color_space = set(coloring)
    color_space -= set([coloring[neighbour] for neighbour in list(G[random_node].keys())])
    color_space -= {coloring[random_node]}
    color_space -= set([x for x in tabuQueue if x[0] == random_node])

    new_color = random.sample(color_space, 1)[0]

    new_coloring = copy.deepcopy(coloring)
    new_coloring[random_node] = new_color
    return (new_coloring, (random_node, new_color))


G = nx.Graph()
n_nodes = 0
n_edges = 0

with open(instanceFileName, "r") as f:
    
    line = f.readline()
    while (len(line.split()) == 0 or line.split()[0] != 'p'):
        line = f.readline()
    
    n_nodes = int(line.split()[2])
    n_edges = int(line.split()[3])
    
    for i in range(n_edges):
        edgeString = f.readline()
        G.add_edge(int(edgeString.split()[1]) - 1, int(edgeString.split()[2]) - 1)


maxIterationsWithoutImprovement = 50 * 20000 * 200 * n_nodes // (n_edges * 28)
numberOfNeighbours = 50
tabuQueueSize = n_nodes*10

coloring = [i for i in range(n_nodes)]

tabuQueue = []

iteration = 0
iterationsWithoutImprovement = 0
bestSolutionValue = n_nodes
currentSolutionValue = n_nodes

timeStart = datetime.datetime.now()

while iterationsWithoutImprovement < maxIterationsWithoutImprovement:
    bestNeighbourValue = len(set(coloring))
    bestNeighbour = coloring
    bestNeighbourChangedNode = None

    for i in range(numberOfNeighbours):
        neighbourColoring, changedNode = generateNeighbour(G, coloring, tabuQueue)
        currentSolutionValue = len(set(neighbourColoring))
        if (currentSolutionValue < bestNeighbourValue):
            bestNeighbourValue = currentSolutionValue
            bestNeighbour = neighbourColoring
            bestNeighbourChangedNode = changedNode
    
    coloring = bestNeighbour
    currentSolutionValue = bestNeighbourValue

    if (currentSolutionValue < bestSolutionValue):
        iterationsWithoutImprovement = 0
        bestSolutionValue = currentSolutionValue
        print(f'[YAY] new best value found: {bestSolutionValue}')

    if (len(tabuQueue) >= tabuQueueSize):
        tabuQueue.pop()
    if (bestNeighbourChangedNode != None):
        tabuQueue.insert(0, bestNeighbourChangedNode)

    iteration += 1
    iterationsWithoutImprovement += 1


seconds = (datetime.datetime.now() - timeStart) / datetime.timedelta(microseconds=1) / 1000000
timeString = f'{floor(max(seconds,0))//60:02d}:{floor(max(seconds,0))%60:02d}'
print(f'time since start: {timeString}')

nx.draw(G, node_color=coloring, with_labels=True)
plt.show()
