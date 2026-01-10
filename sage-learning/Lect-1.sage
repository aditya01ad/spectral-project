## Creating graph from Adgecency List 
# define the graph using a dictionary
my_graph_data = {0 : [1,2], 1 : [3,2], 2 : [4], 3 : [2]}

# Create the grph object
G1 = Graph(my_graph_data)

# Diplay the graphs
G1.show()

## Using built in Graph Genrator

# the complee graph on 5 vertices
K5 = graphs.CompleteGraph(5)
K5.show()
# Cycle graph with 7 vertices
C7 = graphs.CycleGraph(7)
# The Petersen graphs
P = graphs.PetersenGraph()
P.show()