"""
--- Day 12: Digital Plumber ---
Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some programs can't communicate with each other.

Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
In this example, the following programs are in the group that contains program ID 0:

Program 0 by definition.
Program 2, directly connected to program 0.
Program 3 via program 2.
Program 4 via program 2.
Program 5 via programs 6, then 4, then 2.
Program 6 via programs 4, then 2.
Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?

"""
import re

PATTERN = r'(\d+)'

def read_input(filename):
    mapping = {}
    with open(filename) as f:
        for line in f:
            match = re.findall(PATTERN, line)
            mapping[match[0]] = match[1:]
    return mapping

def get_group(_id, programs):
    _id = str(_id)
    seen = set()
    pending = set()
    if _id in programs:
        pending.add(_id)

    while pending:
        current = pending.pop()
        seen.add(current)
        for program in programs[current]:
            if program not in seen and program not in pending:
                pending.add(program)
    return seen

def main():
    programs = read_input('input12.txt')

    group = get_group(0, programs)
    result = len(group)
    print('Part 1 solution:', result)

    # result =
    # print('Part 2 solution:', result)


if __name__ == '__main__':
    main()

