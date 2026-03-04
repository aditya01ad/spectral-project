#from sage.all import Graph
import numpy as np
import itertools
from graph_utils_sage import get_spectrum

def find_gm_switching_partitions(G):
    """
    A heuristic to find a valid partition of vertices for Godsil-McKay switching.
    This version uses Sagemath graph functions.

    It looks for a partition (C, P) where C is an independent set of size 2,
    and P is the rest of the vertices.

    Args:
        G (sage.graphs.graph.Graph): The input graph.

    Yields:
        A dictionary containing the partitioned sets {'C', 'P'} if a
        valid partition is found.
    """
    # G.vertices() returns the list of nodes
    nodes = G.vertices()
    n = len(nodes)

    # Heuristic: Iterate through all pairs of non-adjacent vertices to form set C
    for i in range(n):
        for j in range(i + 1, n):
            u, v = nodes[i], nodes[j]
            
            # Condition: C must be an independent set.
            # G.has_edge() checks for an edge.
            if G.has_edge(u, v):
                continue
            
            C = {u, v}
            P = set(nodes) - C
            
            # Condition: All vertices in P must not be connected to all of C
            # or none of C.
            valid_partition = True
            for node_p in P:
                # G.neighbors() returns the list of neighbors
                neighbors_in_c = len(set(G.neighbors(node_p)) & C)
                if neighbors_in_c == 0 or neighbors_in_c == len(C):
                    valid_partition = False
                    break
            
            if valid_partition:
                # This partition is a candidate for GM switching.
                yield {'C': list(C), 'P': list(P)}


def perform_gm_switching(G, partition):
    """
    Performs the Godsil-McKay switching on a graph given a valid partition.
    This creates a new graph G' which is cospectral to G.

    Args:
        G (sage.graphs.graph.Graph): The original graph.
        partition (dict): A dictionary with keys 'C' and 'P' representing
                          the vertex partition.

    Returns:
        sage.graphs.graph.Graph: The new graph G' after the switching operation.
    """
    # G.copy() creates a copy of the graph
    G_prime = G.copy()
    C, P = partition['C'], partition['P']

    # For each vertex in P, switch its connections to C.
    # If it was connected, disconnect. If it was disconnected, connect.
    for p_node in P:
        for c_node in C:
            if G_prime.has_edge(p_node, c_node):
                # .delete_edge() removes the edge
                G_prime.delete_edge(p_node, c_node)
            else:
                # .add_edge() adds the edge
                G_prime.add_edge(p_node, c_node)
    
    return G_prime


def check_ds_heuristic(G):
    """
    The main heuristic algorithm to check if a graph G is DS (SageMath version).

    It generates potential cospectral mates using GM switching and checks
    if they are non-isomorphic.

    Args:
        G (sage.graphs.graph.Graph): The input graph.

    Returns:
        tuple: (bool, sage.graphs.graph.Graph or None)
               - True if a non-isomorphic cospectral mate is found (G is not DS).
               - False if the search completes without finding one (G may be DS).
               - The second element is the evidence graph if found, otherwise None.
    """
    # 1. Calculate the spectrum of the original graph for later comparison.
    original_spectrum = get_spectrum(G)
    
    # 2. Find candidate partitions for GM switching.
    partition_generator = find_gm_switching_partitions(G)

    # 3. Iterate through partitions, perform switching, and check properties.
    for partition in partition_generator:
        # 3a. Generate the new graph G'
        G_prime = perform_gm_switching(G, partition)

        # 3b. Perform the isomorphism check. In Sagemath, this is a method
        # on the graph object itself.
        if not G.is_isomorphic(G_prime):
            # 3c. As a final confirmation, check if spectra are identical.
            new_spectrum = get_spectrum(G_prime)
            if np.allclose(original_spectrum, new_spectrum):
                # We found a non-isomorphic, cospectral graph.
                # Thus, G is NOT DS.
                return (True, G_prime)

    # If the loop completes without finding any such graph, our heuristic
    # suggests G might be DS.
    return (False, None)
