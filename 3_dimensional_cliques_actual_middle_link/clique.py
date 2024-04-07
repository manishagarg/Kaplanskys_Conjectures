# Copyright (c) [2024] [Manisha Garg]
# Custom License: See LICENSE file in the project root for the full license terms.


import networkx as nx
from itertools import combinations

def has_no_four_cliques(edges):
    """
    Function to check if there are any 4-cliques in a graph.

    :param edges: List of tuples, where each tuple represents an edge.
    :return: False if there is at least one 4-clique, True otherwise.
    """
    G = nx.Graph()
    G.add_edges_from(edges)

    for u, v in G.edges():
        common_neighbors = set(G.neighbors(u)) & set(G.neighbors(v))
        for w, x in combinations(common_neighbors, 2):
            if G.has_edge(w, x):
                return False  # Found a 4-clique, return False immediately

    return True  # No 4-cliques found

# Example usage
#edges_example = [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 4]]
#print(has_no_four_cliques(edges_example))
# 3,4,3
# 3,3,3