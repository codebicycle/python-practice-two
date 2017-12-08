"""
--- Day 6: Memory Reallocation ---

A debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that has been seen before.

For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks, so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on, the 7 blocks are spread out over the memory banks. The fourth, first, and second banks get two blocks each, and the third bank gets one back. The final result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four). Because there are four memory banks, each gets one block. The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, both of which have three blocks. The first bank wins the tie, and its three blocks are distributed evenly over the other three banks, leaving it with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.
At this point, we've reached a state we've seen before: 2 4 1 2 was already seen. The infinite loop is detected after the fifth block redistribution cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?

"""
import itertools

def count_cycles(puzzle_input):
    state = tuple(puzzle_input)
    states = set()
    states.add(state)
    count = itertools.count(start=1)
    for cycle_count in count:
        new_state = redistribute(state)
        if new_state in states:
            break
        states.add(new_state)
        state = new_state

    return cycle_count, list(new_state)

def redistribute(state):
    """Memory reallocation
    Args:
        state (tuple)
    Returns:
        tuple
    """
    state = list(state)
    blocks_to_redistribute = max(state)
    index_max = state.index(blocks_to_redistribute)
    state[index_max] = 0
    index = index_generator(index_max + 1, len(state))
    for i in range(blocks_to_redistribute):
        current = next(index)
        state[current] += 1
    return tuple(state)

def index_generator(start, size):
    index = start
    yield index % size
    while True:
        index += 1
        yield index % size

def read_input(filename):
    with open(filename) as f:
        puzzle_input = tuple(int(column) for column in f.read().split())
    return puzzle_input

def main():
    puzzle_input = read_input('input6.txt')

    result, _ = count_cycles(puzzle_input)
    print(f'Part 1 solution: {result}')


if __name__ == '__main__':
    main()
