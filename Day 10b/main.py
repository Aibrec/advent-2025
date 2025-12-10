from pulp import *
import time

class Machine:
    def __init__(self, target_lights, buttons, joltage_requirements):
        self.buttons = buttons
        self.joltage_requirements = joltage_requirements
        self.lights = [0] * len(target_lights)

    def _try_button_combination(self, presses):
        state = [0] * len(self.joltage_requirements)
        for button_index, num_presses in enumerate(presses):
            for part in self.buttons[button_index]:
                state[part] += num_presses
        return state

    def find_presses_as_linear_combination(self, machine_num):
        button_variables = []
        problem = LpProblem(f'Machine {machine_num}', LpMinimize)
        for i in range(len(self.buttons)):
            button_variables.append(LpVariable(chr(65+i), cat="Integer", lowBound=0))

        # So we have variables for how many times each button is pressed, requirements that they're >=0, and a problem that we're trying to minimize the sum of them
        # Now we want to figure out which buttons add to each index of the joltage_requirements
        for joltage_index, joltage_requirment in enumerate(self.joltage_requirements):
            buttons_involved = []
            vars_involved = []
            for button_index, button in enumerate(self.buttons):
                if joltage_index in button:
                    buttons_involved.append(button_index)
                    vars_involved.append(button_variables[button_index])

            problem += lpSum(vars_involved) == joltage_requirment

        problem += lpSum(button_variables)

        status = problem.solve()
        if status != 1:
            print(f'Status {status}')

        path = []
        for button_variable in button_variables:
            path.append(value(button_variable))
        steps = sum(path)
        return steps, path

def main():
    file_path = 'input.txt'

    start_time = time.perf_counter()
    machines = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split()

            target_lights = parts[0] # Unused in part 2

            joltage_requirements = list([int(n) for n in ((parts[-1])[1:-1]).split(',')])

            button_strings = parts[1:-1]
            buttons = []
            for s in button_strings:
                nums = list([int(n) for n in s[1:-1].split(',')])
                buttons.append(set(nums))

            machines.append(Machine(target_lights, buttons, joltage_requirements))

    total_steps = 0
    for i, machine in enumerate(machines):
        steps, path = machine.find_presses_as_linear_combination(i)
        total_steps += steps
        print(f'Done machine {i}: {steps} | {path}')

    end_time = time.perf_counter()
    time_in_microseconds = (end_time - start_time) * 1000000
    print(f"total steps {total_steps}")
    print(f"took {time_in_microseconds:.2f}μs")
    #20871


main()

