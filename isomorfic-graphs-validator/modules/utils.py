import networkx as nx
import matplotlib.pyplot as plt
from validators import weisfeiler_lehman as wh
from validators import brute_force as bf


def read_adjacency_matrices_from_file(filename: str) -> list[list[list[int]], list[list[int]]]:
    """
    Read two adjacency matrices from input file.
    Matrices are separated by empty line.
    :param filename: file with two adjacency matrices separated by empty line
    :return: list of two adjacency matrices represented as 2-D lists
    """
    adjacency_matrices = []

    with open(filename, 'r') as file:
        adjacency_matrix = []

        for line in file:
            line = line.strip()

            if not line:
                if adjacency_matrix:
                    adjacency_matrices.append(adjacency_matrix)
                    adjacency_matrix = []
            else:
                row = [int(i) for i in line.split()]
                adjacency_matrix.append(row)

        if adjacency_matrix:
            adjacency_matrices.append(adjacency_matrix)

    return adjacency_matrices


def create_graph_from_adjacency_matrix(adjacency_matrix: list[list[int]]) -> nx.Graph:
    """
    Create a graph structure from adjacency matrix
    :param adjacency_matrix: 2-D list
    :return: nx.Graph (graph structure from networkx)
    """
    graph = nx.Graph()

    num_nodes = len(adjacency_matrix)

    graph.add_nodes_from(range(num_nodes))

    for i in range(num_nodes):
        for j in range(num_nodes):
            if adjacency_matrix[i][j] != 0:
                graph.add_edge(i, j, weight=adjacency_matrix[i][j])

    return graph


def plot_graphs(graph1: nx.Graph, graph2: nx.Graph) -> None:
    """
    Visualize the graphs using matplot.
    Graph1 and Graph2 are represented in the left and right halves respectively.
    :param graph1: nx.Graph (graph structure from networkx)
    :param graph2: nx.Graph (graph structure from networkx)
    :return: None
    """

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    axs[0].set_title('Graph 1')
    nx.draw_circular(graph1, with_labels=True, node_color='skyblue', node_size=500, font_size=10, ax=axs[0])

    axs[1].set_title('Graph 2')
    nx.draw_circular(graph2, with_labels=True, node_color='lightgreen', node_size=500, font_size=10, ax=axs[1])

    plt.tight_layout()
    plt.show()


def isomorphism_validator(graph1: nx.Graph, graph2: nx.Graph) -> None:
    """
    Check isomorphism of two graphs using
    Weisfeiler-Lehman and brute force algorithms
    :param graph1: nx.Graph (graph structure from networkx)
    :param graph2: nx.Graph (graph structure from networkx)
    :return: None
    """
    wh_test = wh.isomorphic(graph1, graph2)
    print("\nWeisfeiler-Lehman algorithm: "
          "graphs are " + "not " * (not wh_test) + "isomorphic")

    bf_test = bf.isomorphic(graph1, graph2)
    print("Brute force algorithm: "
          "graphs are " + "not " * (not bf_test) + "isomorphic")

    print("Conclusion: graphs are " + "not " * (not bf_test) + "isomorphic")
