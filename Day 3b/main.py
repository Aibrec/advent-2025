import time

file_path = 'input.txt'

start_time = time.perf_counter()
with open(file_path, 'r') as file:
    banks = []
    for line in file:
        line = line.strip()
        banks.append(list([int(n) for n in line]))

sum_of_banks = 0
num_batteries = 12
for bank in banks:
    power_level = []
    for digit in range(num_batteries):
        max_index = 0
        if bank[max_index] != 9:
            for i in range(1, (len(bank) - (num_batteries-digit)) + 1): # TODO: Figure out if there's an off by one here. Need to leave space for all remaining digits)
                if bank[i] > bank[max_index]:
                    max_index = i
                    if bank[max_index] == 9:
                        break

        power_level.append(bank[max_index])
        bank = bank[max_index+1:]

    bank_power = int("".join([str(n) for n in power_level]))
    #print(f"\tBank power: {bank_power}")
    sum_of_banks += bank_power

end_time = time.perf_counter()
print(f"sum_of_invalid is {sum_of_banks}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.2f}μs")