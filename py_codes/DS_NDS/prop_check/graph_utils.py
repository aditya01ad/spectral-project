import networkx as nx
import numpy as np

def get_spectrum(G):
    """
    Calculates the spectrum (eigenvalues of the adjacency matrix) of a graph.
    The eigenvalues are sorted for consistent comparison.

    Args:
        G (nx.Graph): A NetworkX graph object.

    Returns:
        np.ndarray: A sorted array of the graph's eigenvalues.
    """
    # Use nx.to_numpy_array to ensure consistent node ordering.
    adj_matrix = nx.to_numpy_array(G)
    
    # Use eigvalsh for symmetric matrices, which is faster and more stable.
    eigenvalues = np.linalg.eigvalsh(adj_matrix)
    
    # Sorting ensures that we can compare spectra consistently.
    eigenvalues.sort()
    
    return eigenvalues

def print_graph_invariants(G):
    """
    Prints some basic spectral invariants of a graph.
    These can sometimes be used to quickly distinguish non-cospectral graphs.

    Args:
        G (nx.Graph): The input graph.
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()
    
    adj_matrix = nx.to_numpy_array(G)
    
    # The trace of A^3 is 6 times the number of triangles.
    a_cubed = np.linalg.matrix_power(adj_matrix, 3)
    num_triangles = np.trace(a_cubed) / 6
    
    print(f"  - Vertices (n): {n}")
    print(f"  - Edges (m): {m}")
    print(f"  - Triangles: {int(num_triangles)}")

