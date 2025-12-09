import time

def get_area(p1, p2):
    dx = abs(p1[0] - p2[0]) + 1
    dy = abs(p1[1] - p2[1]) + 1
    area = dx * dy
    return area

def do_lines_cross(vertical_lines, horizontal_lines):
    for vertical_line in vertical_lines:
        for horizontal_line in horizontal_lines:

            # A line is like (3,6), (3,18). A vertical line on x=3 running from y=6 to y=18
            # Our test line could be (1,5), (4,5). A horizontal line on y=5 running from x=1 to x=4
            # They don't intersect as the y=5 is below the minimum of the y=6 to y=18

            # The vertical line runs from vertical_line[0][1] to vertical_line[1][1] with a constant vertical_line[0][0]
            # The horizontal line runs from horizontal_line[0][0] to horizontal_line[1][0] with a constant horizontal_line[0][1]

            # Rectangle (11,1), (2,5). Has side (2,1)->(2,5) (vertical)
            # Should cross line (2,3)->(7,3)

            # If the horizontal line runs at the same height as the vertical line spans
            if vertical_line[0][1] <= horizontal_line[0][1] <= vertical_line[1][1]:
                # And if the vertical line shares an x with the horizontal line
                if horizontal_line[0][0] <= vertical_line[0][0] <= horizontal_line[1][0]:
                    # Then they at least touch. If neither of the points are the same
                    if vertical_line[0] not in horizontal_line and vertical_line[1] not in horizontal_line:
                        return True
    return False

def is_valid(p1, p2, vertical_lines, horizontal_lines):
    # Our rectangle is contained entirely in the lines if it never crosses them
    # TODO: Ignoring the possibility of adjacent lines for now

    # Try shrinking the rectangle a bit so it just won't bump into things
    p1 = list(p1)
    p2 = list(p2)

    if p1[0] < p2[0]:
        p1[0] += 0.1
        p2[0] -= 0.1
    else:
        p1[0] -= 0.1
        p2[0] += 0.1

    if p1[1] < p2[1]:
        p1[1] += 0.1
        p2[1] -= 0.1
    else:
        p1[1] -= 0.1
        p2[1] += 0.1

    p1 = tuple(p1)
    p2 = tuple(p2)

    corners = [
        p1,
        (p1[0], p2[1]),
        p2,
        (p2[0], p1[1])
    ]

    # Constant x
    test_vertical = [
        sorted((corners[0], corners[1])),
        sorted((corners[2], corners[3])),
    ]

    # Constant y
    test_horizontal = [
        sorted((corners[1], corners[2])),
        sorted((corners[3], corners[0]))
    ]

    if not do_lines_cross(test_vertical, horizontal_lines):
        if not do_lines_cross(vertical_lines, test_horizontal):
            return True
    return False

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    red_tiles = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            x,y = [int(n) for n in line.split(',')]
            red_tiles.append((x,y))

    horizontal_lines = []
    vertical_lines = []
    for i in range(len(red_tiles)-1):
        start = red_tiles[i]
        end = red_tiles[i+1]
        line = sorted([start, end])
        if start[0] == end[0]: # Same x, line is vertical
            vertical_lines.append(line)
        elif start[1] == end[1]: # Same y, line is horizontal
            horizontal_lines.append(line)
        else:
            raise ValueError('Weird line')

    start = red_tiles[-1]
    end = red_tiles[0]
    line = sorted([start, end])
    if start[0] == end[0]:  # Same x, line is vertical
        vertical_lines.append(line)
    elif start[1] == end[1]:  # Same y, line is horizontal
        horizontal_lines.append(line)
    else:
        raise ValueError('Weird line')

    #test = is_valid((11,1), (2,5), vertical_lines, horizontal_lines)

    max_area = 0
    for outer in range(len(red_tiles)):
        for inner in range(outer+1, len(red_tiles)):
            box_one = red_tiles[outer]
            box_two = red_tiles[inner]
            area = get_area(box_one, box_two)

            if area > max_area:
                #if box_one == (11,1) and box_two == (2,5):
                #    print('ok')

                if is_valid(box_one, box_two, vertical_lines, horizontal_lines):
                    print(f"For {box_one}, {box_two} area = {area}")
                    max_area = area

    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"max_area {max_area}")
    print(f"took {time_in_microseconds:.2f}μs")

    # Not 226712183, which was too low. Likely need to handle adjacent lines. Could also be internal meaningless lines and we need to do a polygon simplification.
    # Was 1569262188 trying with a shurnk rectangle
    # Not 2194273018, unknown if it was high or low
    # Not 2447743140, which was too high. Can't just drop the = sign on <=.
    # Not 2927152935, what was too high. Can't just ignore 1 error each
main()

