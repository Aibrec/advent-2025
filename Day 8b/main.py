import math
import time

class Pointer:
    circuit = None
    def __init__(self, circuit):
        self.circuit = circuit


def getDistance(p1, p2):
    dx = (p1[0] - p2[0]) ** 2
    dy = (p1[1] - p2[1]) ** 2
    dz = (p1[2] - p2[2]) ** 2
    d = math.sqrt(dx+dy+dz)
    return d

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    boxes = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            x,y,z = [int(n) for n in line.split(',')]
            boxes.append((x,y,z))

    # If the input was bigger I'd do an octree but this finishes near instantly
    distances = []
    for outer in range(len(boxes)):
        for inner in range(outer+1, len(boxes)):
            box_one = boxes[outer]
            box_two = boxes[inner]
            distance = getDistance(box_one, box_two)
            distances.append((distance, (box_one, box_two)))

    distances = sorted(distances)

    box_to_circuit = {}
    connection_num = 0
    while True:
        distance, new_connection = distances[connection_num]
        box_one, box_two = new_connection

        #print(f"{connection_num}: was {box_one} to {box_two} at distance {distance}")

        matching_circuits = []

        if box_one in box_to_circuit:
            matching_circuits.append(box_to_circuit[box_one].circuit)

        if box_two in box_to_circuit:
            matching_circuits.append(box_to_circuit[box_two].circuit)

        if not matching_circuits:
            circuit = {box_one, box_two}
            pointer = Pointer(circuit)
            box_to_circuit[box_one] = pointer
            box_to_circuit[box_two] = pointer

        elif len(matching_circuits) == 1:
            circuit = matching_circuits[0]
            circuit.add(box_one)
            circuit.add(box_two)

            if box_one in box_to_circuit:
                box_to_circuit[box_one].circuit = circuit
                box_to_circuit[box_two] = box_to_circuit[box_one]
            else:
                box_to_circuit[box_two].circuit = circuit
                box_to_circuit[box_one] = box_to_circuit[box_two]
        else:
            circuit_one = matching_circuits[0]
            circuit_two = matching_circuits[1]
            if circuit_one != circuit_two:
                if len(circuit_one) < len(circuit_two):
                    circuit_one,circuit_two = circuit_two,circuit_one # Make sure circuit_one is the larger set

                circuit_one.update(circuit_two)
                circuit = circuit_one

                box_to_circuit[box_one].circuit = circuit
                box_to_circuit[box_two].circuit = circuit

        connection_num += 1
        if len(circuit) == len(boxes):
            print(f'All boxes in circuit on connect {connection_num}. Last connection was {box_one, box_two}')
            answer = box_one[0] * box_two[0]
            print(f'Answer is {answer}')
            break

    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"took {time_in_microseconds:.2f}μs")
    #started off taking took 635826.80μs
    #skipping equal circuits down to took 516772.40μs
    #the whole pointer thing brought it down to like 511445.00μs and was not worth it
main()

