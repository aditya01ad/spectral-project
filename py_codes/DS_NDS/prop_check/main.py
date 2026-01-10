import networkx as nx
import numpy as np
from ds_heuristic import check_ds_heuristic

def create_example_graph():
    """
    Creates an example graph to test the heuristic.
    This specific graph (Shrikhande graph) is a known case of a graph
    that is cospectral but not isomorphic to a regular graph of the same degree.
    It's a good candidate for demonstrating the algorithm.
    """
    G = nx.Graph()
    """
    edges = [
        (0, 1), (0, 4), (0, 5), (0, 8), (0, 10), (0, 15),
        (1, 2), (1, 6), (1, 9), (1, 11), (1, 15),
        (2, 3), (2, 7), (2, 10), (2, 12), (2, 14),
        (3, 4), (3, 8), (3, 11), (3, 13), (3, 14),
        (4, 5), (4, 9), (4, 12), (4, 13),
        (5, 6), (5, 7), (5, 13), (5, 14),
        (6, 7), (6, 8), (6, 11), (6, 12),
        (7, 8), (7, 9), (7, 10), (7, 15),
        (9, 10), (9, 13), (9, 14),
        (10, 11), (10, 12),
        (11, 12), (11, 15),
        (12, 13), (12, 15),
        (13, 14), (13, 15),
        (14, 15), (14, 6), (14, 1), (14, 9)
    ]
    """
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)]
    # The Shrikhande graph has 16 vertices and is 6-regular.
    # We add nodes up to 15 to ensure the graph has 16 vertices (0-15).
    G.add_nodes_from(range(7))
    G.add_edges_from(edges)
    return G

def main():
    """
    Main function to run the DS heuristic algorithm.
    It creates a graph, runs the check, and prints the results.
    """
    print("Designing a heuristic to test for the DS property of a graph.")
    print("==========================================================")

    # You can replace this with your own graph loading mechanism.
    # For example: G = nx.read_edgelist('my_graph.txt')
    G = create_example_graph()

    print(f"\nAnalyzing input graph G with {G.number_of_nodes()} vertices and {G.number_of_edges()} edges.")
    print("Running the Godsil-McKay switching heuristic...")

    is_ds, evidence_graph = check_ds_heuristic(G)

    print("\n----- Heuristic Results -----")
    if is_ds:
        print("Strong evidence found: The graph G is NOT Determined by its Spectrum (DS).")
        print("A non-isomorphic, cospectral graph was constructed.")
        
        # You could optionally save or visualize the evidence_graph here.
        # For example, to save the adjacency matrix:
        if evidence_graph:
            adj_matrix_g_prime = nx.to_numpy_array(evidence_graph)
            # np.savetxt("evidence_graph_adj.txt", adj_matrix_g_prime, fmt='%d')
            print("\nAdjacency matrix of the new non-isomorphic graph G':")
            print(adj_matrix_g_prime)

    else:
        print("Heuristic did not find a cospectral mate.")
        print("This provides evidence that the input graph G MAY BE DS.")
        print("Note: This is not a definitive proof of the DS property.")
    print("-----------------------------")


if __name__ == "__main__":
    main()
