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
    complete_rotations = abs(turn) // 100
    at_zero_count += complete_rotations
    if turn > 0:
        turn = turn % 100
        if turn + dial >= 100:
            at_zero_count += 1
    elif turn < 0 and dial != 0:
        turn = turn % -100
        if turn + dial <= 0:
            at_zero_count += 1

    dial = (dial + turn) % 100
    #print(f"Turn: {turn}, Dial: {dial}, Times at 0: {at_zero_count}")

end = time.perf_counter()
print(f"at_zero_count is {at_zero_count}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")