# Hamming graph H(q,q) in Sage

def HammingGraph(q):
    # vertices = all q-tuples over {0,...,q-1}
    vertices = CartesianProduct([range(q)]*q)

    # create empty graph
    G = Graph(multiedges=False, loops=False)
    G.add_vertices(vertices)

    # add edges: differ in exactly one coordinate
    for u in vertices:
        for v in vertices:
            if u != v:
                # count number of coordinates they differ in
                diff = sum(1 for i in range(q) if u[i] != v[i])
                if diff == 1:
                    G.add_edge(u, v)

    return G

# Example: H(3,3)
G = HammingGraph(3)
print(G)
G.show()

