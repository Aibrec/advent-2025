import time

def compress_ranges(ranges):
    ranges_sorted_by_start = list(sorted(ranges, key=lambda r: r[0]))
    compressed_ranges = []
    for i in range(len(ranges_sorted_by_start)-1):
        current_range = ranges_sorted_by_start[i]
        next_range = ranges_sorted_by_start[i+1]
        if current_range[1] >= next_range[0]:
            combined_range = (current_range[0], max(current_range[1], next_range[1]))
            #print(f"Merged {current_range} and {next_range} to {combined_range}")
            ranges_sorted_by_start[i+1] = combined_range
        else:
            compressed_ranges.append(current_range)
            #print(f"Didn't merge {current_range} and {next_range}\n")

    if compressed_ranges[-1] != ranges_sorted_by_start[-1]:
        compressed_ranges.append(ranges_sorted_by_start[-1])

    return compressed_ranges

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    ranges = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            parts = line.split('-')
            start = int(parts[0])
            end = int(parts[1])
            ranges.append((start, end))

    compressed_ranges = compress_ranges(ranges)
    total_fresh = 0
    for r in compressed_ranges:
        range_fresh = r[1] - r[0] + 1
        total_fresh += range_fresh
        #print(f"{r[0]}-{r[1]} had {range_fresh} fresh")

    end_time = time.perf_counter()
    print(f"fresh_count is {total_fresh}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
main()

