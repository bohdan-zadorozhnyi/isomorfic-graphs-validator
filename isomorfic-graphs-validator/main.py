from modules import utils
import os.path


def main():
    choice = ""
    examples = ["example1.txt", "example2.txt", "example3.txt"]

    print("------------------------------------------")
    print("Welcome to the Isomorphic Graphs Validator program!")
    print("I am here to help you to define whether the graphs are isomorphic.\n"
          "I use Weisfeiler-Lehman and brute force algorithms.\n"
          "WL algorithm: fast, not always efficient\n"
          "Brute force algorithm: gives accurate information, computationally consuming")

    while choice != 5:
        print("------------------------------------------")
        print("Menu:")
        print("1 - Show example 1\n"
              "2 - Show example 2\n"
              "3 - Show example 3\n"
              "4 - Enter file with graphs to validate\n"
              "5 - Exit the program")
        print("------------------------------------------")

        choice = input("Choose the option(1-5): ")
        if choice in "123":
            filename = "examples/" + examples[int(choice) - 1]
        elif choice == "4":
            print("\nFile should have adjacency matrices of two graphs separated by the empty line")
            filename = input("Enter file name: ")
            if not os.path.exists(filename):
                print("There is no such file!")
                continue
        elif choice == "5":
            break
        else:
            print("------------------------------------------")
            print("There is no such option!")
            continue

        adjacency_matrices = utils.read_adjacency_matrices_from_file(filename)

        graph1 = utils.create_graph_from_adjacency_matrix(adjacency_matrices[0])
        graph2 = utils.create_graph_from_adjacency_matrix(adjacency_matrices[1])

        utils.isomorphism_validator(graph1, graph2)

        visualize = input("\nDo you want to visualize graphs (y-yes/any other input-no): ")
        if visualize == "y" or visualize == "Y":
            utils.plot_graphs(graph1, graph2)


if __name__ == '__main__':
    main()
