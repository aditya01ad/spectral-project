# import display helper
from display_utils import disp_graph, print_graph
from pathlib import Path
out_dir = Path('matches')
out_dir.mkdir(exist_ok=True)

n = 5
# build target graph g on n+1 vertices
#g = graphs.CompleteGraph(n-1)
#g = graphs.CycleGraph(4)
#g = Graph(n)
#g.add_edges([(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)])
#g.add_vertex(n-1)
#g.add_edge((0, n-1))

edges1 = [(0, 1), (0, 2), (0, 3), (0, 4)]
g = Graph(edges1)

A = g.adjacency_matrix()
print_graph(g)

# compute target spectrum (as Python floats) and simple invariants
target_spectrum = sorted([float(x) for x in g.spectrum()])
target_degseq = sorted(g.degree())
from collections import Counter
target_mult = Counter([round(x, 6) for x in target_spectrum])

#print('target degrees:', target_degseq)
#print('target spectrum (rounded):', [float('{:.4f}'.format(x)) for x in target_spectrum])


# iterate non-isomorphic graphs on n+1 vertices and count isospectral ones
count = 0
matches = []
total = 0



# graphs(n+1) yields non-isomorphic graphs
for h in graphs(n):
    total += 1

    if g.size() != h.size() :
        continue
    # quick prune: degree sequence must match
    if sorted(h.degree()) != target_degseq :
        continue
    # next prune: compare multiplicity histogram of rounded eigenvalues
    hs = sorted([float(x) for x in h.spectrum()])
    if Counter([round(x,6) for x in hs]) != target_mult:
        continue
    if g.edges() == h.edges() : 
        continue 
    # final check: compare numeric multisets within tolerance
    # since both lists are sorted, we can compare elementwise with tolerance
    tol = 1e-6
    ok = all(abs(a - b) <= tol for a, b in zip(hs, target_spectrum))
    if ok:
        count += 1
        matches.append(h.graph6_string())
        # save a plot for this matched graph
        filename = out_dir / f'match_{count}.png'
        disp_graph(h, save=str(filename), layout='spring')
        print('saved plot to', filename)

print('examined', total, 'graphs on', n, 'vertices; found', count, 'isospectral graphs')
for s in matches:
    print(s)

print("\n count = ", count)

