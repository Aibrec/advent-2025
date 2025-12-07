import time
import math

def do_operator(operator, numbers):
    result = 0
    if operator is not None:
        if operator == '*':
            result = math.prod(numbers)
        elif operator == '+':
            result =  sum(numbers)
        else:
            raise ValueError(f'Unrecognized operator {operator}')
    #print(f'Op {operator}: {numbers} = {result}')
    return result

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    worksheet = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line[:-1]
            worksheet.append(line)

    total = 0
    total_columns = max(len(s) for s in worksheet)
    total_rows = len(worksheet)

    current_operator = None
    current_numbers = []
    for c in range(total_columns):
        num = ""
        for r in range(total_rows-1):
            if c < len(worksheet[r]) and worksheet[r][c] != ' ':
                num += worksheet[r][c]

        if c < len(worksheet[total_rows-1]) and worksheet[total_rows-1][c] != ' ':
            total += do_operator(current_operator, current_numbers)
            current_operator = worksheet[total_rows-1][c]
            current_numbers = []

        if num:
            current_numbers.append(int(num))

    total += do_operator(current_operator, current_numbers)

    end_time = time.perf_counter()
    print(f"total is {total}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
main()

