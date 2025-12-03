import time

file_path = 'input.txt'

start_time = time.perf_counter()
with open(file_path, 'r') as file:
    banks = []
    for line in file:
        line = line.strip()
        banks.append(line)

sum_of_banks = 0
for bank in banks:
    first_digit = len(bank) - 2
    second_digit = len(bank) - 1
    for i in reversed(range(len(bank)-2)):
        if bank[i] >= bank[first_digit]:
            second_digit = first_digit if bank[first_digit] > bank[second_digit] else second_digit
            first_digit = i
    bank_power = int(f"{bank[first_digit]}{bank[second_digit]}")
    print(f"Bank: {bank}")
    print(f"\tBank power: {bank_power}")
    sum_of_banks += bank_power

end_time = time.perf_counter()
print(f"sum_of_invalid is {sum_of_banks}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.2f}μs")