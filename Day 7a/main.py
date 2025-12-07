import time
from collections import defaultdict
from bisect import bisect_left

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    splitters = defaultdict(list)
    beams = defaultdict(set)
    with open(file_path, 'r') as file:
        y = 0
        for line in file:
            line = line.strip()
            for x, char in enumerate(line):
                if char == '^':
                    splitters[x].append(y)
                elif char == 'S':
                    beams[0].add(x)
            y += 1

    splitters_used = set()
    total_lines = y
    for y in range(total_lines):
        for beam_x in beams[y]:
            splitters_in_column = splitters[beam_x]
            first_splitter_down = bisect_left(splitters_in_column, y)
            if first_splitter_down < len(splitters_in_column):
                next_splitter_y = splitters_in_column[first_splitter_down]
                splitters_used.add((next_splitter_y, beam_x))
                for new_beam_x in (beam_x + 1, beam_x - 1):
                    if 0 <= new_beam_x: # Can ignore the max because it's just an empty row
                        beams[next_splitter_y+1].add(new_beam_x)

    total_splitters_used = len(splitters_used)
    end_time = time.perf_counter()
    print(f"total_splitters_used is {total_splitters_used}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
main()

