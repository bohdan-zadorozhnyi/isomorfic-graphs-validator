import networkx as nx


def weisfeiler_lehman(graph: nx.Graph) -> dict:
    """
    Perform the Weisfeiler-Lehman label propagation algorithm on the graph.
    Description:
        Use a label propagation scheme to iteratively update
        the node labels based on the local neighborhood structure.
        The algorithm:
        1. Initialize each node's label with its initial label.
        2. Iterate until the labels converge:
           a. For each node in the graph, collect the labels of its neighbors.
           b. Sort the neighbor labels and concatenate them into a string.
           c. Update the label of the current node by appending the sorted neighbor labels.
        3. Return the final labels for each node in the graph.
    :param graph: nx.Graph (graph structure from networkx)
    :return: dict
    """
    labels = nx.get_node_attributes(graph, 'label')

    while True:
        updated_labels = {}

        for node in graph.nodes():
            current_label = labels.get(node, '')
            neighbor_labels = [labels.get(neighbor, '') for neighbor in graph.neighbors(node)]
            sorted_labels = ''.join(sorted(neighbor_labels))
            updated_labels[node] = current_label + sorted_labels

        if updated_labels == labels:
            break

        labels = updated_labels

    return labels


def isomorphic(graph1: nx.Graph, graph2: nx.Graph) -> bool:
    """
    Check isomorphism of two graphs using the Weisfeiler-Lehman algorithm.
    Compare the labels of both graphs after performing the Weisfeiler-Lehman
    label propagation algorithm on each of them.
    If labels are the same, then the graphs are isomorphic.
    Otherwise, the graphs are not isomorphic.
    :param graph1: nx.Graph (graph structure from networkx)
    :param graph2: nx.Graph (graph structure from networkx)
    :return: bool
    """
    if graph1.number_of_nodes() != graph2.number_of_nodes() or graph1.number_of_edges() != graph2.number_of_edges():
        return False

    labels1 = weisfeiler_lehman(graph1)
    labels2 = weisfeiler_lehman(graph2)

    return labels1 == labels2
