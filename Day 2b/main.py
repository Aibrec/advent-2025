import time
#import re

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

def check_number_is_any_pattern(num):
    num = str(num)
    for pattern_length in range(1, (len(num) // 2)+1):
        if len(num) % pattern_length != 0:
            continue

        for start_index in range(0, pattern_length):
            indexes_that_should_be_the_same = range(start_index+pattern_length, len(num), pattern_length)
            for repeating_index in indexes_that_should_be_the_same:
                if num[start_index] != num[repeating_index]:
                    break # We break if there is a mismatch
            else:
                continue # Which bypasses the break below
            break # So this is a break for the mismatch, as it shows this pattern length is invalid
        else:
            # If there was no break, this pattern length is valid
            return True
    return False

# def string_is_pattern(pattern, string):
#     pattern_length = len(pattern)
#     for i in range(0, len(string), pattern_length):
#         substring = string[i:i+pattern_length]
#         if substring != pattern:
#             return False
#     return True

# def check_number_is_any_pattern(num):
#     num = str(num)
#
#     for i in range(1, (len(num) // 2)+1):
#         part = num[0:i]
#         if string_is_pattern(part, num[i:]):
#             return True
#         #if re.match(rf'^({part})+$', num):
#         #    return True
#     return False

sum_of_invalid = 0
for r in ranges:
    start, end = r
    for i in range(start, end+1):
        if check_number_is_any_pattern(i):
            #print(f"match: {i}")
            sum_of_invalid += i

end_time = time.perf_counter()
print(f"sum_of_invalid is {sum_of_invalid}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.2f}μs")