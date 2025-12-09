import math
import time

def getArea(p1, p2):
    dx = abs(p1[0] - p2[0]) + 1
    dy = abs(p1[1] - p2[1]) + 1
    area = dx * dy
    return area

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    red_tiles = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            x,y = [int(n) for n in line.split(',')]
            red_tiles.append((x,y))

    max_area = 0
    for outer in range(len(red_tiles)):
        for inner in range(outer+1, len(red_tiles)):
            box_one = red_tiles[outer]
            box_two = red_tiles[inner]
            area = getArea(box_one, box_two)
            print(f"For {box_one}, {box_two} area = {area}")
            if area > max_area:
                max_area = area


    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"max_area {max_area}")
    print(f"took {time_in_microseconds:.2f}μs")
main()

