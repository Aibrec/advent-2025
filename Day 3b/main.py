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
    power_level = list(bank[len(bank)-num_batteries:])
    for i in reversed(range(len(bank)-num_batteries)):
        if bank[i] >= power_level[0]:
            new_number = bank[i]
            for d in range(len(power_level)):
                if power_level[d] <= new_number:
                    power_level[d], new_number = new_number, power_level[d]
                else:
                    break
    bank_power = int("".join([str(n) for n in power_level]))
    #print(f"Bank: {bank}")
    #print(f"\tBank power: {bank_power}")
    sum_of_banks += bank_power

end_time = time.perf_counter()
print(f"sum_of_invalid is {sum_of_banks}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.2f}μs")