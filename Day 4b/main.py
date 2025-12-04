import time

def get_adjacent(coords):
    adjacent = []
    for y in (-1,0,1):
        for x in (-1,0,1):
            if x != 0 or y != 0:
                adjacent.append((coords[0]+y, coords[1]+x))
    return adjacent

def get(grid, coord):
    if 0 <= coord[0] < len(grid):
        if 0 <= coord[1] < len(grid[coord[0]]):
            return grid[coord[0]][coord[1]]
    return None

def remove_paper(grid, coords_to_consider):
    papers_removed = set()
    coords_to_consider_next_time = set()
    for coord in coords_to_consider:
        adjacent_coords = get_adjacent(coord)
        adjacent_values = list([get(grid, adj_coord) for adj_coord in adjacent_coords])
        if adjacent_values.count('@') < 4:
            grid[coord[0]][coord[1]] = '.'
            papers_removed.add(coord)
            for adj_coord in adjacent_coords:
                if get(grid, adj_coord) == '@': # Should use the values we already got somehow
                    coords_to_consider_next_time.add(adj_coord)

    coords_to_consider_next_time -= papers_removed
    return papers_removed, coords_to_consider_next_time

def find_papers(grid):
    papers = set()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                papers.add((y,x))
    return papers

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    with open(file_path, 'r') as file:
        grid = []
        for line in file:
            line = line.strip()
            grid.append(list([c for c in line]))

    accessible_paper = 0
    coords_to_consider = find_papers(grid)
    while True:
        papers_removed, coords_to_consider = remove_paper(grid, coords_to_consider)
        if papers_removed:
            accessible_paper += len(papers_removed)
        else:
            break

    end_time = time.perf_counter()
    print(f"accessible_paper is {accessible_paper}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")

main()

