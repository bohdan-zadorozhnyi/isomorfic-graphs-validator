from itertools import permutations


def isomorphic(graph1, graph2):
    """
    Check isomorphism of two graphs using the brute force algorithm.
    Description:
        Generate all possible permutations of node mappings between the two
        graphs and check if each permutation satisfies the isomorphism condition.
        1. Check if the number of nodes and edges are the same.
        2. Generate all possible permutations of node mappings between graph1 and graph2.
        3. For each permutation, check if the edges in graph1 are preserved under the node mapping in graph2.
        If all edges are preserved for any permutation, then the graphs are isomorphic.
        Otherwise, the graphs are not isomorphic.
    :param graph1: nx.Graph (graph structure from networkx)
    :param graph2: nx.Graph (graph structure from networkx)
    :return: bool
    """
    if graph1.number_of_nodes() != graph2.number_of_nodes() or graph1.number_of_edges() != graph2.number_of_edges():
        return False

    nodes1 = list(graph1.nodes())
    nodes2 = list(graph2.nodes())

    node_mappings = list(permutations(nodes2))

    for mapping in node_mappings:
        node_map = dict(zip(nodes1, mapping))

        if all(graph2.has_edge(node_map[u], node_map[v]) for u, v in graph1.edges()):
            return True

    return False
