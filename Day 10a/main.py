import time
import itertools

class Machine:
    def __init__(self, target_lights, buttons, joltage_requirements):
        self.target_lights = target_lights
        self.buttons = buttons
        self.joltage_requirements = joltage_requirements
        self.lights = [0] * len(target_lights)

    def _try_button_combination(self, button_indexes):
        state = [0] * len(self.target_lights)
        for button_index in button_indexes:
            for part in self.buttons[button_index]:
                state[part] = 1 - state[part]
        return state

    def find_presses(self):
        for steps in range(1,len(self.buttons)+1):
            for combination in itertools.combinations(range(len(self.buttons)), steps):
                resulting_state = self._try_button_combination(combination)
                if resulting_state == self.target_lights:
                    return steps, combination
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
            target_lights = list([int(n) for n in target_lights])

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

