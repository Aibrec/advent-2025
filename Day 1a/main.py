import time

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    turns = []
    for line in file:
        direction = line[0]
        number = int(line[1:])
        if direction == 'L':
            turns.append(number*-1)
        elif direction == 'R':
            turns.append(number)

dial = 50
at_zero_count = 0
for turn in turns:
    dial = (dial+turn) % 100
    if dial == 0:
        at_zero_count +=1

end = time.perf_counter()
print(f"at_zero_count is {at_zero_count}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")