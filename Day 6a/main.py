import time

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    worksheet = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split()
            worksheet.append(parts)

    total = 0
    operators = worksheet[-1]
    worksheet = worksheet[:-1]
    for column_num, operator in enumerate(operators):
        subtotal = int(worksheet[0][column_num])
        for row in worksheet[1:]:
            num = int(row[column_num])
            if operator == '*':
                subtotal *= num
            elif operator == '+':
                subtotal += num
            else:
                raise ValueError(f'Unrecognized operator {operator}')
        total += subtotal

    end_time = time.perf_counter()
    print(f"fresh_count is {total}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
main()

