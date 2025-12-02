import time

file_path = 'input.txt'

start_time = time.perf_counter()
with open(file_path, 'r') as file:
    ranges = []
    line = file.read()
    for group in line.split(','):
        parts = group.split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))

def check_number_is_twice_a_pattern(num):
    num = str(num)
    if len(num) % 2 != 0:
        return False

    first_half = num[0:len(num)//2]
    second_half = num[len(num)//2:]

    if first_half != second_half:
        return False

    return True

sum_of_invalid = 0
for r in ranges:
    start, end = r
    for i in range(start, end+1):
        if check_number_is_twice_a_pattern(i):
            print(f"match: {i}")
            sum_of_invalid += i

end_time = time.perf_counter()
print(f"sum_of_invalid is {sum_of_invalid}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.2f}μs")