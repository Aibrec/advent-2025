from pulp import *
import time
import networkx as nx

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
    paths = list(nx.all_simple_paths(graph, 'you', 'out'))

    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"total steps {len(paths)}")
    print(f"took {time_in_microseconds:.2f}μs")

main()

