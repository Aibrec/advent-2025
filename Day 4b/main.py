import time

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
    papers = set()
    with open(file_path, 'r') as file:
        y = 0
        for line in file:
            line = line.strip()
            for x, char in enumerate(line):
                if char == '@':
                    papers.add((y,x))
            y += 1

    starting_papers = len(papers)
    coords_to_consider = papers.copy()
    while True:
        papers, coords_to_consider = remove_paper(papers, coords_to_consider)
        if not coords_to_consider:
            break

    end_time = time.perf_counter()
    print(f"accessible_paper is {starting_papers - len(papers)}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
    # brute version took something like 3000000
    # faster version took 59925.70μs
    # set version took 35959.80μs
main()

