from sage.all import Graph, graphs
import numpy as np
from ds_heuristic_sage import check_ds_heuristic

def create_example_graph():
    """
    Creates an example graph to test the heuristic using SageMath.
    This specific graph (Shrikhande graph) is a known case of a graph
    that is cospectral but not isomorphic to a regular graph of the same degree.
    """
    # Sagemath's ShrikhandeGraph() generator makes this easy.
    # It is cospectral with the 16-vertex rook's graph.
    G = graphs.ShrikhandeGraph()
    return G

def main():
    """
    Main function to run the DS heuristic algorithm using SageMath.
    It creates a graph, runs the check, and prints the results.
    """
    print("Designing a heuristic to test for the DS property of a graph (SageMath Version).")
    print("============================================================================")

    # You can replace this with your own graph loading mechanism.
    # For example: G = Graph('my_graph.g6')
    G = create_example_graph()

    print(f"\nAnalyzing input graph G with {G.num_verts()} vertices and {G.num_edges()} edges.")
    print("Running the Godsil-McKay switching heuristic...")

    is_not_ds, evidence_graph = check_ds_heuristic(G)

    print("\n----- Heuristic Results -----")
    if is_not_ds:
        print("Strong evidence found: The graph G is NOT Determined by its Spectrum (DS).")
        print("A non-isomorphic, cospectral graph was constructed.")
        
        # You could optionally save or visualize the evidence_graph here.
        if evidence_graph:
            # .numpy() converts the Sagemath matrix to a numpy array for printing
            adj_matrix_g_prime = evidence_graph.adjacency_matrix().numpy()
            # np.savetxt("evidence_graph_adj.txt", adj_matrix_g_prime, fmt='%d')
            print("\nAdjacency matrix of the new non-isomorphic graph G':")
            print(adj_matrix_g_prime)

    else:
        print("Heuristic did not find a cospectral mate.")
        print("This provides evidence that the input graph G MAY BE DS.")
        print("Note: This is not a definitive proof of the DS property.")
    print("-----------------------------")


if __name__ == "__main__":
    # This script is intended to be run within a Sagemath environment
    # (e.g., `sage -python main_sage.py` or inside a Sage notebook)
    main()
