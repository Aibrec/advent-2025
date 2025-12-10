import time
from collections import  deque


class Machine:
    def __init__(self, target_lights, buttons, joltage_requirements):
        self.target_lights = target_lights
        self.buttons = buttons
        self.joltage_requirements = joltage_requirements
        self.lights = [0] * len(target_lights)

    def find_presses(self):
        starting_state = '0' * len(self.target_lights)
        states_to_explore = deque([(starting_state, 0, "")])
        seen_states = {starting_state}
        while states_to_explore:
            state, steps, path = states_to_explore.popleft()
            for button in self.buttons:
                new_state = list([c for c in state])
                for button_num in button:
                    new_state[button_num] = '0' if new_state[button_num] == '1' else '1'
                new_state = "".join(new_state)

                new_path = f"{path} | {button}"
                if new_state == self.target_lights:
                    return steps+1, new_path

                if new_state not in seen_states:
                    seen_states.add(new_state)
                    states_to_explore.append((new_state, steps+1, new_path))
        raise ValueError('No path found')

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    machines = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split()

            target_lights = parts[0]
            target_lights = target_lights[1:-1]
            target_lights = target_lights.replace('.', '0')
            target_lights = target_lights.replace('#', '1')
            #target_lights = list([int(n) for n in target_lights])

            joltage_requirements = parts[-1]

            button_strings = parts[1:-1]
            buttons = []
            for s in button_strings:
                nums = list([int(n) for n in s[1:-1].split(',')])
                buttons.append(sorted(nums))

            machines.append(Machine(target_lights, buttons, joltage_requirements))

    total_steps = 0
    for machine in machines:
        steps, path = machine.find_presses()
        total_steps += steps

    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"total steps {total_steps}")
    print(f"took {time_in_microseconds:.2f}μs")


main()

