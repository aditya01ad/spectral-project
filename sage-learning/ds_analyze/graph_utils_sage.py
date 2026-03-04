import numpy as np
#from sage.all import Graph

def create_G_n_k(n,k):
    Kn = graphs.CompleteGraph(n)
    g = Kn
    for i in range(k) :
        g.add_vertex(n+i)
        g.add_edge(i,n+i)
    return g

def get_spectrum(G):
    """
    Calculates the spectrum (eigenvalues of the adjacency matrix) of a graph.
    The eigenvalues are sorted for consistent comparison.
    
    Args:
        G (sage.graphs.graph.Graph): A SageMath graph object.

    Returns:
        np.ndarray: A sorted array of the graph's eigenvalues.
    """
    # Sagemath's G.spectrum() method is highly optimized and returns
    # a sorted list of floating-point eigenvalues.
    eigenvalues = G.spectrum()
    
    # Convert to numpy array for consistent comparison with np.allclose
    return np.array(eigenvalues)

def print_graph_invariants(G):
    """
    Prints some basic spectral invariants of a graph using SageMath functions.

    Args:
        G (sage.graphs.graph.Graph): The input graph.
    """
    # .num_verts() and .num_edges() are the Sagemath equivalents
    n = G.num_verts()
    m = G.num_edges()
    
    # Get the adjacency matrix as a Sagemath matrix
    adj_matrix = G.adjacency_matrix()
    
    # Sagemath matrices support direct exponentiation and .trace()
    a_cubed = adj_matrix**3
    num_triangles = a_cubed.trace() / 6
    
    print(f"  - Vertices (n): {n}")
    print(f"  - Edges (m): {m}")
    print(f"  - Triangles: {int(num_triangles)}")
