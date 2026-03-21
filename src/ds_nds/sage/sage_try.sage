# Graph 1: The Star Graph
edges1 = [(0, 1), (0, 2), (0, 3), (0, 4)]
g1 = Graph(edges1)

# Graph 2: 4-cycle and an isolated vertex
edges2 = [(0, 1), (1, 2), (2, 3), (3, 0)] # C4
g2 = Graph(edges2)
g2.add_vertex(4) # K1

# Verify they are non-isomorphic but have the same spectrum
print(f"Are they isomorphic? {g1.is_isomorphic(g2)}")
print(f"Spectrum of g1: {g1.spectrum()}")
print(f"Spectrum of g2: {g2.spectrum()}")

# g1.show()
# g2.show()