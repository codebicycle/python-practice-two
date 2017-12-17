"""
--- Day 17: Spinlock ---
Suddenly, whirling in the distance, you notice what looks like a massive, pixelated hurricane: a deadly spinlock. This spinlock isn't just consuming computing power, but memory, too; vast, digital mountains are being ripped from the ground and consumed by the vortex.

If you don't move quickly, fixing that printer will be the least of your problems.

This spinlock's algorithm is simple but efficient, quickly consuming everything in its path. It starts with a circular buffer containing only the value 0, which it marks as the current position. It then steps forward through the circular buffer some number of steps (your puzzle input) before inserting the first new value, 1, after the value it stopped on. The inserted value becomes the current position. Then, it steps forward from there the same number of steps, and wherever it stops, inserts after it the second new value, 2, and uses that as the new current position again.

It repeats this process of stepping forward, inserting a new value, and using the location of the inserted value as the new current position a total of 2017 times, inserting 2017 as its final operation, and ending with a total of 2018 values (including 0) in the circular buffer.

For example, if the spinlock were to step 3 times per insert, the circular buffer would begin to evolve like this (using parentheses to mark the current position after each iteration of the algorithm):

(0), the initial state before any insertions.
0 (1): the spinlock steps forward three times (0, 0, 0), and then inserts the first value, 1, after it. 1 becomes the current position.
0 (2) 1: the spinlock steps forward three times (0, 1, 0), and then inserts the second value, 2, after it. 2 becomes the current position.
0  2 (3) 1: the spinlock steps forward three times (1, 0, 2), and then inserts the third value, 3, after it. 3 becomes the current position.
And so on:

0  2 (4) 3  1
0 (5) 2  4  3  1
0  5  2  4  3 (6) 1
0  5 (7) 2  4  3  6  1
0  5  7  2  4  3 (8) 6  1
0 (9) 5  7  2  4  3  8  6  1
Eventually, after 2017 insertions, the section of the circular buffer near the last insertion looks like this:

1512  1134  151 (2017) 638  1513  851
Perhaps, if you can identify the value that will ultimately be after the last value written (2017), you can short-circuit the spinlock. In this example, that would be 638.

What is the value after 2017 in your completed circular buffer?

Your puzzle input is 304.

"""
def spinlock(times, step):
    state = [0]
    position = 0
    for value in range(1, times+1):
        insertion_index = ((position + step) % len(state)) + 1
        state.insert(insertion_index, value)
        position = insertion_index
    return state

def value_after(value, state):
    position = state.index(value)
    next_position = (position + 1) % len(state)
    return state[next_position]

def value_after_zero(times, step):
    """Compute the value after 0 from the spinlock algorithm.
    0 is always on the first position, index zero.
    The value after 0 sits at index one.

    """
    value_at_index_one = None
    virtual_length = 1
    position = 0
    for value in range(1, times+1):
        insertion_index = ((position + step) % virtual_length) + 1
        if insertion_index == 1:
            value_at_index_one = value
        position = insertion_index
        virtual_length += 1
    return value_at_index_one

def read_input(filename):
    with open(filename) as f:
        puzzle_input = int(f.read())
    return puzzle_input

def main():
    puzzle_input = read_input('input17.txt')

    state_2017 = spinlock(times=2017, step=puzzle_input)
    result = value_after(2017, state_2017)
    print('Part 1 solution:', result)

    result = value_after_zero(times=50_000_000, step=puzzle_input)
    print('Part 2 solution:', result)


if __name__ == '__main__':
    main()
