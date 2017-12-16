"""
--- Day 16: Permutation Promenade ---
You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places.
For example, with only five programs standing in a line (abcde), they could do the following dance:

s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?

--- Part Two ---
Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc, and use the same dance moves:

s1, a spin of size 1: cbaed.
x3/4, swapping the last two programs: cbade.
pe/b, swapping programs e and b: ceadb.
In what order are the programs standing after their billion dances?

"""
import re


SPIN = r's(\d+)'
EXCHANGE = r'x(\d+)/(\d+)'
PARTNER = r'p(\w)/(\w)'

def parse(instruction):
    match = re.match(SPIN, instruction)
    if match:
        number = int(match.group(1))
        return 's', number
    match = re.match(EXCHANGE, instruction)
    if match:
        position_a = int(match.group(1))
        position_b = int(match.group(2))
        return 'x', position_a, position_b
    match = re.match(PARTNER, instruction)
    if match:
        program_a = match.group(1)
        program_b = match.group(2)
        return 'p', program_a, program_b
    raise ValueError(f'Unknown instruction {instruction}.')

def spin(number, state):
    state[:number], state[number:] = state[-number:], state[:-number]

def exchange(position_a, position_b, state):
    state[position_a], state[position_b] = state[position_b], state[position_a]

def partner(program_a, program_b, state):
    position_a = state.index(program_a)
    position_b = state.index(program_b)
    exchange(position_a, position_b, state)

MAPPING = {'s': spin,
           'x': exchange,
           'p': partner,}

def interpret_instruction(parsed_instruction, state):
    instruction_code = parsed_instruction[0]
    arguments = parsed_instruction[1:]
    function = MAPPING[instruction_code]
    function(*arguments, state=state)

def interpret(instructions, state):
    for instruction in instructions:
        parsed_instruction = parse(instruction)
        interpret_instruction(parsed_instruction, state)

def read_input(filename):
    with open(filename) as f:
        instructions = [instruction.strip() for instruction in f.read().split(',')]

    return instructions

def loop_length(instructions, initial_state):
    state = initial_state.copy()
    count = 0
    while True:
        count += 1
        interpret(instructions, state)
        if state == initial_state:
            break
    return count

def repeat(instructions, times, initial_state):
    state = initial_state.copy()
    for _ in range(times):
        interpret(instructions, state)
    return state

def main():
    instructions = read_input('input16.txt')
    initial_state = list('abcdefghijklmnop')

    final_state = repeat(instructions, times=1, initial_state=initial_state)
    result = ''.join(final_state)
    print('Part 1 solution:', result)

    loop = loop_length(instructions, initial_state)
    times = 1_000_000_000
    times = times % loop
    final_state = repeat(instructions, times, initial_state)
    result = ''.join(final_state)
    print('Part 2 solution:', result)

if __name__ == '__main__':
    main()
