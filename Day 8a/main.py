import math
import time

def getDistance(p1, p2):
    dx = (p1[0] - p2[0]) ** 2
    dy = (p1[1] - p2[1]) ** 2
    dz = (p1[2] - p2[2]) ** 2
    d = math.sqrt(dx+dy+dz)
    return d

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    boxes = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            x,y,z = [int(n) for n in line.split(',')]
            boxes.add((x,y,z))

    complete_boxes = set()
    distances = []
    for box_one in boxes:
        for box_two in (boxes - complete_boxes):
            if box_one != box_two:
                distance = getDistance(box_one, box_two)
                distances.append((distance, (box_one, box_two)))
        complete_boxes.add(box_one)

    distances = sorted(distances, reverse=True)

    box_to_circuit = {}
    for connection_num in range(1000):
        distance, new_connection = distances.pop()
        box_one, box_two = new_connection

        #print(f"{connection_num}: was {box_one} to {box_two} at distance {distance}")

        matching_circuits = []

        if box_one in box_to_circuit:
            matching_circuits.append(box_to_circuit[box_one])

        if box_two in box_to_circuit:
            matching_circuits.append(box_to_circuit[box_two])

        if not matching_circuits:
            circuit = {box_one, box_two}
        elif len(matching_circuits) == 1:
            circuit = matching_circuits[0]
            circuit.add(box_one)
            circuit.add(box_two)
        else:
            circuit_one = matching_circuits[0]
            circuit_two = matching_circuits[1]
            if len(circuit_one) < len(circuit_two):
                circuit_one,circuit_two = circuit_two,circuit_one # Make sure circuit_one is the larger set

            circuit_one.update(circuit_two)
            for box in circuit_two:
                box_to_circuit[box] = circuit_one
            circuit = circuit_one
        box_to_circuit[box_one] = circuit
        box_to_circuit[box_two] = circuit

    circuits = set([frozenset(c) for c in box_to_circuit.values()])
    largest_circuits = []
    for i in range(3):
        largest_circuit = max(circuits, key=len)
        largest_circuits.append(largest_circuit)
        circuits.remove(largest_circuit)

    total = 1
    for circuit in largest_circuits:
        total *= len(circuit)

    end_time = time.perf_counter()
    print(f"Multiple of size of 3 largest {total}")
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
main()

