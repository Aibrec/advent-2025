import time
from functools import cache

def flip_horizontally(shape):
    flipped = set()

    # Wow is there ever a better way to do this
    mappings = {
        (0,0): (0,2),
        (0,1): (0,1),
        (0,2): (0,0),

        (1,0): (1, 2),
        (1,1): (1, 1),
        (1,2): (1, 0),

        (2,0): (2,2),
        (2,1): (2,1),
        (2,2): (2,0),
    }

    for start,end in mappings.items():
        if start in shape:
            flipped.add(end)

    return flipped

def rotate_by_90_degrees(shape):
    rotated = set()

    # Wow is there ever a better way to do this
    mappings = {
        (0,0): (0,2),
        (0,1): (1,2),
        (0,2): (2,2),

        (1,0): (0,1),
        (1,1): (1,1),
        (1,2): (2,1),

        (2,0): (0,0),
        (2,1): (1,0),
        (2,2): (2,0),
    }

    for start,end in mappings.items():
        if start in shape:
            rotated.add(end)

    return frozenset(rotated)

def generate_rotated_shapes(shape):
    rotated_shapes = [frozenset(shape)]
    for i in range(3):
        rotated_shapes.append(rotate_by_90_degrees(rotated_shapes[-1]))
    return rotated_shapes

def print_shape(shape):
    for y in range(3):
        line = ""
        for x in range(3):
            if (y,x) in shape:
                line += '#'
            else:
                line += '.'
        print(line)
    print()

scoring_points = [
    (0,0), (0,1), (0,2), (1,1), (2,1)
]

@cache
def shapes_that_can_fit(shapes, occupied):
    can_fit = []
    for shape in shapes:
        if combined := can_fit_in_3x3(shape, occupied):
            # Score based on how many of the left and top are filled for
            score = sum([1 for scoring_point in scoring_points if scoring_point in combined])
            can_fit.append((score, shape))

    sorted(can_fit)
    return list([can_fit[1] for can_fit in can_fit])

@cache
def can_fit_in_3x3(shape, occupied):
    obstructions = occupied.intersection(shape)
    if obstructions:
        return False
    else:
        return frozenset(shape+occupied)

def get_3x3_around_point(y, x, occupied):
    area_around_point = set()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            adjusted_point = (y+dy, x+dx)
            if adjusted_point in occupied:
                area_around_point.add((dy+1, dx+1))
    return frozenset(area_around_point)

def fit_shapes(max_y, max_x, y, x, inventory, shapes, blocked):
    # We places form the middle of shapes so just shave 2 off the max x and y to allow for that
    start_x = 0
    start_y = 0

    occupied_set = set()

def main():
    file_path = 'input.txt'
    start_time = time.perf_counter()

    shapes = []
    regions = []
    with open(file_path, 'r') as file:
        # Get the shapes
        shape_lines = []
        for line in file:
            line = line.strip()
            if not line:
                if len(shapes) == 6:
                    break
                continue

            if line[1] == ':':
                continue

            shape_lines.append(line)
            if len(shape_lines) == 3:
                shape = set()
                for y, shape_line in enumerate(shape_lines):
                    for x, char in enumerate(shape_line):
                        if char == '#':
                            shape.add((y,x))
                shapes.append(shape)
                shape_lines = []

        # Get the regions
        for line in file:
            line = line.strip()
            area, required_shapes = line.split(':')
            area_x, area_y = [int(num) for num in area.split('x')]
            required_shapes = [int(num) for num in required_shapes.split()]
            regions.append(((area_y, area_x), required_shapes))

    all_shapes = set()
    for n, shape in enumerate(shapes):
        rotated_shapes = generate_rotated_shapes(shape)
        # print(f"{n}: ")
        # for shape in rotated_shapes:
        #     print_shape(shape)
        all_shapes.update(rotated_shapes)

        flipped_shape = flip_horizontally(shape)
        rotated_flipped_shapes = generate_rotated_shapes(flipped_shape)
        all_shapes.update(rotated_flipped_shapes)

    #NM: This doesn't keep a mapping to inventory so it's all bunk. Need a class
    all_shapes = frozenset(all_shapes)
    total_paths = paths_with_dac_first + paths_with_fft_first
    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"total paths {total_paths}")
    print(f"took {time_in_microseconds:.2f}μs")

main()

