from pulp import *
import time
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

def save_graph(graph, name):
    fig = plt.figure(figsize=(100, 200))
    nx.draw(graph, with_labels=True, pos=nx.spring_layout(graph, k=1), ax=fig.add_subplot())
    #matplotlib.use('Agg')
    fig.savefig(f"{name}.png")

def main():
    file_path = 'input.txt'
    start_time = time.perf_counter()

    connections_by_machine = {}
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            machine = line[:3]
            connections = line[5:].split()
            connections_by_machine[machine] = connections

            for connection in connections:
                edges.append((machine, connection))

    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    # There are no paths from dac to fft
    # So valid paths must go svr -> fft -> dac-> out
    # There are no loops, so anything after dac doesn't have to be considered in the earlier parts

    paths_from_dac_to_out = list(nx.all_simple_paths(graph, 'dac', 'out'))
    num_paths_from_dac_to_out = len(paths_from_dac_to_out) # 5317 on my input

    # Remove the later nodes to simplify the later search
    nodes_after_dac = list(nx.descendants(graph, 'dac'))
    for node in nodes_after_dac:
        if node == 'dac':
            continue
        graph.remove_node(node)

    # On the reverse graph it'll run fft -> svr
    reversed_graph = graph.reverse()
    paths_from_fft_to_svr = list(nx.all_simple_paths(reversed_graph, 'fft', 'svr'))
    num_paths_from_fft_to_svr = len(paths_from_fft_to_svr) # 4275 on my input

    # save_graph(graph, "fft_to_dac_graph")

    # Remove the later nodes to simplify the later search
    nodes_before_fft = list(nx.descendants(reversed_graph, 'fft'))
    for node in nodes_before_fft:
        if node == 'fft':
            continue
        graph.remove_node(node)

    # As everything goes forward, dac is the only node that should have not outgoing edges and matter. Let's remove them.
    while True:
        end_nodes = [node for node in graph.nodes if graph.out_degree(node) == 0 and node != 'dac']
        if not end_nodes:
            break

        for end_node in end_nodes:
            graph.remove_node(end_node)

    reversed_graph = graph.reverse()
    # Ditto but for fft on the reversed graph
    while True:
        end_nodes = [node for node in reversed_graph.nodes if reversed_graph.out_degree(node) == 0 and node != 'fft']
        if not end_nodes:
            break

        for end_node in end_nodes:
            reversed_graph.remove_node(end_node)

    graph = reversed_graph.reverse()

    # Still too many paths but I can't see any more structure in the image.
    # Whatever run time is 129593229.60μs =~ 2 mintues
    #save_graph(graph, "fft_to_dac_graph_ends_removed")
    # num_paths_from_fft_to_dac = 0
    # for path in nx.all_simple_paths(graph, 'fft', 'dac'):
    #     print(f'A path is {path}')
    #     num_paths_from_fft_to_dac += 1

    paths_from_fft_to_dac = list(nx.all_simple_paths(graph, 'fft', 'dac'))
    num_paths_from_fft_to_dac = len(paths_from_fft_to_dac) # 17109136
    print(f'num_paths_from_fft_to_dac {num_paths_from_fft_to_dac}')

    total_paths = num_paths_from_dac_to_out * num_paths_from_fft_to_svr * num_paths_from_fft_to_dac
    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"total paths {total_paths}")
    print(f"took {time_in_microseconds:.2f}μs")

main()

