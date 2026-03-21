import numpy as np
import networkx as nx
from itertools import permutations

def find_cospectral_graphs(v, e):
    """
    Finds all classes of cospectral, non-isomorphic graphs for a given
    number of vertices and edges.

    Args:
        v (int): The number of vertices for the graphs.
        e (int): The number of edges for the graphs.

    Returns:
        list: A list of lists, where each inner list contains a set of
              adjacency matrices of cospectral, non-isomorphic graphs.
              Returns an empty list if no such classes are found.
    """
    # --- Step 1: Generate all unique permutations of edges/non-edges ---
    num_possible_edges = v * (v - 1) // 2
    
    if e > num_possible_edges or e < 0:
        print(f"Error: Number of edges for {v} vertices must be between 0 and {num_possible_edges}.")
        return []

    # Create the base list of 1s (edges) and 0s (non-edges)
    base_list = [1] * e + [0] * (num_possible_edges - e)
    
    # Use a set to store only the unique permutations of the base list
    unique_permutations = set(permutations(base_list))

    # --- Step 2: Initialize data structures ---
    M = []  # To store all generated adjacency matrices
    C = []  # The final list of cospectral classes
    P = {}  # A dictionary to map characteristic polynomials to indices in C

    # --- Step 3: Build adjacency matrices from permutations ---
    for p in unique_permutations:
        adj_matrix = np.zeros((v, v), dtype=int)
        k = 0 # Index for the permutation list
        # Iterate through the upper triangle of the matrix
        for i in range(v):
            for j in range(i + 1, v):
                adj_matrix[i, j] = p[k]
                # Make the matrix symmetric for an undirected graph
                adj_matrix[j, i] = p[k]
                k += 1
        M.append(adj_matrix)

    # --- Step 4: Classify matrices by polynomial and check for isomorphism ---
    for matrix in M:
        # Calculate the characteristic polynomial.
        # We get the coefficients from the eigenvalues and round them to handle
        # floating point inaccuracies. We use a tuple of coefficients as a
        # hashable dictionary key.
        # Use eigvalsh for symmetric matrices: faster and returns real values.
        eigenvalues = np.linalg.eigvalsh(matrix)
        poly_coeffs = np.poly(eigenvalues)
        poly_tuple = tuple(np.round(poly_coeffs, decimals=5))

        if poly_tuple in P:
            # 4(a): This polynomial has been seen before.
            # Get the index of the corresponding cospectral class in C.
            alpha = P[poly_tuple]
            current_graph = nx.from_numpy_array(matrix)
            is_isomorphic_to_existing = False
            
            # Check if the new graph is isomorphic to any graph already in its class.
            for existing_matrix in C[alpha]:
                existing_graph = nx.from_numpy_array(existing_matrix)
                if nx.is_isomorphic(current_graph, existing_graph):
                    is_isomorphic_to_existing = True
                    break
            
            # If it's not isomorphic to any existing members, add it to the class.
            if not is_isomorphic_to_existing:
                C[alpha].append(matrix)
        else:
            # 4(b): This is a new characteristic polynomial.
            # Map the new polynomial to the index of the new class we're about to create.
            P[poly_tuple] = len(C)
            # Create a new cospectral class in C containing the current matrix.
            C.append([matrix])

    # --- Step 5: Return the result ---
    # Filter the results to include only the non-trivial classes, i.e., those
    # containing more than one non-isomorphic graph.
    cospectral_classes = [cls for cls in C if len(cls) > 1]
    
    return cospectral_classes

def print_results(cospectral_classes):
    """A helper function to print the results in a readable format."""
    if not cospectral_classes:
        print("No sets of cospectral, non-isomorphic graphs were found.")
        return
        
    print(f"Found {len(cospectral_classes)} class(es) of cospectral graphs.\n")
    for i, cls in enumerate(cospectral_classes):
        print("-" * 30)
        print(f"Class {i + 1} (contains {len(cls)} graphs)")
        print("-" * 30)
        for j, matrix in enumerate(cls):
            print(f"Graph {j + 1}:")
            print(matrix)
            print()

# --- Example Usage ---
if __name__ == '__main__':
    # A classic example: graphs with 5 vertices and 6 edges.
    # This may take a few seconds to compute.
    # print("Finding cospectral graphs for v=5, e=6...")
    # v_val = 5
    # e_val = 6
    # result_classes = find_cospectral_graphs(v_val, e_val)
    # print_results(result_classes)

    # Another example: v=6, e=6
    print("\n" + "="*40 + "\n")
    print("Finding cospectral graphs for v=6, e=6...")
    v_val = 6
    e_val = 6
    result_classes = find_cospectral_graphs(v_val, e_val)
    print_results(result_classes)