import time
from collections import defaultdict
from bisect import bisect_left


def get_adjacent(coords):
    adjacent = set()
    for y in (-1,0,1):
        for x in (-1,0,1):
            if x != 0 or y != 0:
                adjacent.add((coords[0]+y, coords[1]+x))
    return adjacent

def remove_paper(papers, papers_to_consider):
    papers_to_consider_next_time = set()
    for coord in papers_to_consider:
        adj_coords = get_adjacent(coord)
        adj_papers = adj_coords.intersection(papers)
        if len(adj_papers) < 4:
            papers.remove(coord)
            papers_to_consider_next_time.update(adj_papers)

    papers_to_consider_next_time = papers_to_consider_next_time.intersection(papers)
    return papers, papers_to_consider_next_time

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    splitters = defaultdict(list)
    beams = defaultdict(lambda: defaultdict(int))
    with open(file_path, 'r') as file:
        y = 0
        for line in file:
            line = line.strip()
            for x, char in enumerate(line):
                if char == '^':
                    splitters[x].append(y)
                elif char == 'S':
                    beams[0][x] = 1
            y += 1

    total_lines = y
    worlds_at_neg_1 = 0
    beams_at_bottom = 0
    for y in range(total_lines):
        for beam_x, worlds_in_beam in beams[y].items():
            splitters_in_column = splitters[beam_x]
            first_splitter_down = bisect_left(splitters_in_column, y)
            if first_splitter_down < len(splitters_in_column):
                next_splitter_y = splitters_in_column[first_splitter_down]
                for new_beam_x in (beam_x + 1, beam_x - 1):
                    if 0 <= new_beam_x: # Can ignore the max because it's just an empty row
                        beams[next_splitter_y+1][new_beam_x] += worlds_in_beam
                    else:
                        worlds_at_neg_1 += worlds_in_beam
            else:
                beams_at_bottom += worlds_in_beam

    total_beams = beams_at_bottom + worlds_at_neg_1
    end_time = time.perf_counter()
    print(f"total_beams is {total_beams}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
main()

