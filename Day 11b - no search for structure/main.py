import time
from functools import cache

def main():
    file_path = 'input.txt'
    start_time = time.perf_counter()

    connections_by_machine = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            machine = line[:3]
            connections = line[5:].split()
            connections_by_machine[machine] = connections

    @cache
    def num_paths(start, end):
        if start == end:
            return 1

        paths = 0
        for connection in connections_by_machine.get(start, []):
            paths += num_paths(connection, end)
        return paths

    paths_with_dac_first = num_paths('svr', 'dac') * num_paths('dac', 'fft') * num_paths('fft', 'out')
    paths_with_fft_first = num_paths('svr', 'fft') * num_paths('fft', 'dac') * num_paths('dac', 'out')

    total_paths = paths_with_dac_first + paths_with_fft_first
    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"total paths {total_paths}")
    print(f"took {time_in_microseconds:.2f}μs")

main()

