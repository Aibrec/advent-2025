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

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    with open(file_path, 'r') as file:
        grid = []
        for line in file:
            line = line.strip()
            grid.append(line)

    accessible_paper = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                adjacent_coords = get_adjacent((y,x))
                adjacent_values = list([get(grid, coord) for coord in adjacent_coords])
                if adjacent_values.count('@') < 4:
                    accessible_paper += 1
                    #print(f'Accessible at {y},{x}')

    end_time = time.perf_counter()
    print(f"accessible_paper is {accessible_paper}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")

main()

