import time

def get_adjacent(coords):
    adjacent = set()
    for y in (-1,0,1):
        for x in (-1,0,1):
            if x != 0 or y != 0:
                adjacent.add((coords[0]+y, coords[1]+x))
    return adjacent

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    papers = {}
    with open(file_path, 'r') as file:
        y = 0
        for line in file:
            line = line.strip()
            for x, char in enumerate(line):
                if char == '@':
                    papers[(y,x)] = 0
            y += 1

    starting_papers = len(papers)
    removable_papers = set()
    for coord in papers.keys():
        for adj_coord in get_adjacent(coord):
            if adj_coord in papers:
                papers[coord] += 1
        if papers[coord] < 4:
            removable_papers.add(coord)

    while removable_papers:
        removeable_paper = removable_papers.pop()
        del papers[removeable_paper]
        for adj_coord in get_adjacent(removeable_paper):
            if adj_coord in papers:
                papers[adj_coord] -= 1
                if papers[adj_coord] == 3:
                    removable_papers.add(adj_coord)

    end_time = time.perf_counter()
    print(f"accessible_paper is {starting_papers - len(papers)}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
    # brute version took something like 3000000
    # faster version took 59925.70μs
    # set version took 35959.80μs
    # dict version took 33087.90μs
main()

