import time

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    ranges = []
    ingredients = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            parts = line.split('-')
            start = int(parts[0])
            end = int(parts[1])
            ranges.append((start, end))

        for line in file:
            line = line.strip()
            ingredients.append(int(line))

    fresh_count = 0
    for ingredient in ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                fresh_count += 1
                print(f'Fresh: {ingredient} due to {start},{end}')
                break

    end_time = time.perf_counter()
    print(f"fresh_count is {fresh_count}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
main()

