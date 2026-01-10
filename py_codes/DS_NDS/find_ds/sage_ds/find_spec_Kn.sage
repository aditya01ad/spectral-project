m = 15;
for n in range(5, m):
    g = graphs.CompleteGraph(n)
    g.add_vertex(n)
    g.add_edge((0, n))
    A = g.adjacency_matrix()
    spectrum = g.spectrum()
    print([float('{:.4f}'.format) for l in spectrum])

    # This will create an iterator for all non-isomorphic graphs on 7 vertices
graphs_n7 = graphs(7)

# To see the graphs, you can convert the iterator to a list
list_of_graphs = list(graphs_n7)
count = 0
# To print each graph (for example, in graph6 format)
for h in list_of_graphs:
    if g.spectrum() == h.spectrum() : 
        print(h.graph6_string())
        count = count + 1