"""
--- Day 24: Electromagnetic Moat ---

The CPU itself is a large, black building surrounded by a bottomless pit. Enormous metal tubes extend outward from the side of the building at regular intervals and descend down into the void. There's no way to cross, but you need to get inside.

No way, of course, other than building a bridge out of the magnetic components strewn about nearby.

Each component has two ports, one on each end. The ports come in all different types, and only matching types can be connected. You take an inventory of the components by their port types (your puzzle input). Each port is identified by the number of pins it uses; more pins mean a stronger connection for your bridge. A 3/7 component, for example, has a type-3 port on one side, and a type-7 port on the other.

Your side of the pit is metallic; a perfect surface to connect a magnetic, zero-pin port. Because of this, the first port you use must be of type 0. It doesn't matter what type of port you end with; your goal is just to make the bridge as strong as possible.

The strength of a bridge is the sum of the port types in each component. For example, if your bridge is made of components 0/3, 3/7, and 7/4, your bridge has a strength of 0+3 + 3+7 + 7+4 = 24.

For example, suppose you had the following components:

0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10

With them, you could make the following valid bridges:

    0/1
    0/1--10/1
    0/1--10/1--9/10
    0/2
    0/2--2/3
    0/2--2/3--3/4
    0/2--2/3--3/5
    0/2--2/2
    0/2--2/2--2/3
    0/2--2/2--2/3--3/4
    0/2--2/2--2/3--3/5

(Note how, as shown by 10/1, order of ports within a component doesn't matter. However, you may only use each port on a component once.)

Of these bridges, the strongest one is 0/1--10/1--9/10; it has a strength of 0+1 + 1+10 + 10+9 = 31.

What is the strength of the strongest bridge you can make with the components you have available?

"""
from collections import defaultdict

def make_adjacency_list(items):
    adjacency_list = defaultdict(set)
    for item in items:
        a, b = item
        adjacency_list[a].add(item)
        adjacency_list[b].add(item)
    return adjacency_list

def build_bridge(adjacency_list):
    max_score = 0
    max_bridge = None

    def build(pins, bridge):
        nonlocal max_score
        nonlocal max_bridge
        candidates = adjacency_list[pins] - set(bridge)
        if not candidates:
            return bridge

        for candidate in candidates:
            new_bridge = bridge + [candidate]
            new_pins = get_free_end(candidate, pins)
            new_bridge = build(new_pins, new_bridge)
            if not new_bridge:
                continue
            new_score = score(new_bridge)
            if new_score > max_score:
                max_score = new_score
                max_bridge = new_bridge
        return max_bridge

    initial_pins = 0
    initial_bridge = []
    build(initial_pins, initial_bridge)
    return max_score, max_bridge

def build_longest_bridge(adjacency_list):
    max_score = 0
    max_length = 0
    longest_bridge = None

    def build(pins, bridge):
        nonlocal max_score
        nonlocal max_length
        nonlocal longest_bridge
        candidates = adjacency_list[pins] - set(bridge)
        if not candidates:
            return bridge

        for candidate in candidates:
            new_bridge = bridge + [candidate]
            new_pins = get_free_end(candidate, pins)
            new_bridge = build(new_pins, new_bridge)
            if not new_bridge:
                continue
            new_length = len(new_bridge)
            new_score = score(new_bridge)
            if (new_length, new_score) > (max_length, max_score):
                max_length = new_length
                longest_bridge = new_bridge
                max_score = new_score
        return longest_bridge

    initial_pins = 0
    initial_bridge = []
    build(initial_pins, initial_bridge)
    return max_score, longest_bridge

def score(bridge):
    return sum(end for component in bridge for end in component)

def get_free_end(component, used_end):
    if component[0] == used_end:
        return component[1]
    return component[0]

def read_input(filename):
    with open(filename) as f:
        puzzle_input = [tuple(int(x) for x in line.split('/'))
                        for line in f]
    return puzzle_input

def main():
    components = read_input('input24.txt')
    adjacency_list = make_adjacency_list(components)

    max_score, max_bridge = build_bridge(adjacency_list)
    print('Part 1 solution:', max_score)

    max_score, _ = build_longest_bridge(adjacency_list)
    print('Part 2 solution:', max_score)


if __name__ == '__main__':
    main()
