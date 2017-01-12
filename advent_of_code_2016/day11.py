"""
--- Day 11: Radioisotope Thermoelectric Generators ---

You come upon a column of four floors that have been entirely sealed off from the rest of the building except for a small dedicated lobby. There are some radiation warnings and a big sign which reads "Radioisotope Testing Facility".

According to the project status board, this facility is currently being used to experiment with Radioisotope Thermoelectric Generators (RTGs, or simply "generators") that are designed to be paired with specially-constructed microchips. Basically, an RTG is a highly radioactive rock that generates electricity through heat.

The experimental RTGs have poor radiation containment, so they're dangerously radioactive. The chips are prototypes and don't have normal radiation shielding, but they do have the ability to generate an electromagnetic radiation shield when powered. Unfortunately, they can only be powered by their corresponding RTG. An RTG powering a microchip is still dangerous to other microchips.

In other words, if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be fried. Therefore, it is assumed that you will follow procedure and keep chips connected to their corresponding RTG when they're in the same room, and away from other RTGs otherwise.

These microchips sound very interesting and useful to your current activities, and you'd like to try to retrieve them. The fourth floor of the facility has an assembling machine which can make a self-contained, shielded computer for you to take with you - that is, if you can bring it all of the RTGs and microchips.

Within the radiation-shielded part of the facility (in which it's safe to have these pre-assembly RTGs), there is an elevator that can move between the four floors. Its capacity rating means it can carry at most yourself and two RTGs or microchips in any combination. (They're rigged to some heavy diagnostic equipment - the assembling machine will detach it for you.) As a security measure, the elevator will only function if it contains at least one RTG or microchip. The elevator always stops on each floor to recharge, and this takes long enough that the items within it and the items on that floor can irradiate each other. (You can prevent this if a Microchip and its Generator end up on the same floor in this way, as they can be connected while the elevator is recharging.)

You make some notes of the locations of each component of interest (your puzzle input). Before you don a hazmat suit and start moving things around, you'd like to have an idea of what you need to do.

When you enter the containment area, you and the elevator will start on the first floor.

For example, suppose the isolated area has the following arrangement:

The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.

As a diagram (F# for a Floor number, E for Elevator, H for Hydrogen, L for Lithium, M for Microchip, and G for Generator), the initial state looks like this:

F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM

Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:

    Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:

    F4 .  .  .  .  .
    F3 .  .  .  LG .
    F2 E  HG HM .  .
    F1 .  .  .  .  LM

    Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip is getting power from its generator:

    F4 .  .  .  .  .
    F3 E  HG HM LG .
    F2 .  .  .  .  .
    F1 .  .  .  .  LM

    Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you so you can still use the elevator:

    F4 .  .  .  .  .
    F3 .  HG .  LG .
    F2 E  .  HM .  .
    F1 .  .  .  .  LM

    At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect each other:

    F4 .  .  .  .  .
    F3 .  HG .  LG .
    F2 .  .  .  .  .
    F1 E  .  HM .  LM

    Bring both Microchips up one floor, where there is nothing to fry them:

    F4 .  .  .  .  .
    F3 .  HG .  LG .
    F2 E  .  HM .  LM
    F1 .  .  .  .  .

    Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding generators while the elevator recharges, preventing either of them from being fried:

    F4 .  .  .  .  .
    F3 E  HG HM LG LM
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Bring both Microchips to the fourth floor:

    F4 E  .  HM .  LM
    F3 .  HG .  LG .
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can still use the elevator; this is safe because although the Lithium Generator is on the destination floor, you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:

    F4 .  .  .  .  LM
    F3 E  HG HM LG .
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible Microchip to the Lithium Generator upon arrival:

    F4 E  HG .  LG LM
    F3 .  .  HM .  .
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Bring the Lithium Microchip with you to the third floor so you can use the elevator:

    F4 .  HG .  LG .
    F3 E  .  HM .  LM
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Bring both Microchips to the fourth floor:

    F4 E  HG HM LG LM
    F3 .  .  .  .  .
    F2 .  .  .  .  .
    F1 .  .  .  .  .

In this arrangement, it takes 11 steps to collect all of the objects at the fourth floor for assembly. (Each elevator stop counts as one step, even if nothing is added to or removed from it.)

In your situation, what is the minimum number of steps required to bring all of the objects to the fourth floor?

"""
from pprint import pprint

import itertools

import math

FAIL = []


def is_valid(floor):
    chips = [element for element in floor if element[1] == 'M']
    generators = [element for element in floor if element[1] == 'G']
    if chips and generators:
        for chip in chips:
            if chip[0] + 'G' not in generators:
                return False
    return True


def is_goal(state):
    elevator = state[-1]
    return (len(state[0]) == len(state[1]) == len(state[2]) == 0
            and len(state[3]) != 0)


def heuristic(state):
    rank = 3 * len(state[0]) // 2 + 2 * len(state[1]) // 2 + 1 * len(state[2]) // 2
    elevator = state[-1]
    return rank + elevator


def optimize(floor):
    """Keep only one generator, microchip pair"""
    simplified_floor = floor[:]

    groups = set(itertools.combinations(floor, 2))
    pairs = [(x, y)
             for (x, y) in groups
             if x[0] == y[0] and x[1] != y[1]]

    pairs_minus_one = pairs[:-1]
    if pairs_minus_one:
        extraneous_elements = [element
                               for pair in pairs_minus_one
                               for element in pair]
        simplified_floor = set(floor) - set(extraneous_elements)
        groups = set(itertools.combinations(simplified_floor, 2))

    single_combinations = itertools.combinations(simplified_floor, 1)
    groups.update(single_combinations)
    return groups


def successors(state):
    successors = {}
    elevator = state[-1]
    current_floor = state[elevator]

    # groups = set(itertools.combinations(current_floor, 2))
    # single_combinations = itertools.combinations(current_floor, 1)
    # groups.update(single_combinations)

    groups = optimize(current_floor)

    directions = []
    if elevator + 1 < 4:
        directions.append((elevator + 1, 'up'))

    if elevator - 1 >= 0:
        directions.append((elevator - 1, 'down'))

    for direction in directions:
        new_elevator, label = direction
        for group in groups:
            current_floor_after = tuple(set(current_floor) - set(group))
            # current_floor_after = tuple(element
            #                             for element in current_floor
            #                             if element not in group)
            if not is_valid(current_floor_after):
                continue
            arriving_floor = state[new_elevator]
            arriving_floor_after = tuple(set(arriving_floor) | set(group))
            # arriving_floor_after = arriving_floor + group
            if not is_valid(arriving_floor_after):
                continue

            new_state = list(state)
            new_state[-1] = new_elevator
            new_state[elevator] = current_floor_after
            new_state[new_elevator] = arriving_floor_after
            new_state = tuple(new_state)

            successors[new_state] = group + direction
    return successors


def shortest_path(start, successors, heuristic):
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [[start]]
    solutions = []
    while frontier:
        frontier.sort(key=lambda p: heuristic(p[-1]))
        path = frontier.pop(0)
        current_state = path[-1]
        for cell in successors(current_state):
            new_path = path + [cell]
            if is_goal(cell):
                solutions.append(new_path)
                print()
                print(len(new_path) - 1, len(explored))
                # pprint(path_repr(new_path))
                return solutions
            elif cell not in explored:
                explored.add(cell)
                frontier.append(new_path)
    return solutions


def state_repr(state):
    floors = [','.join(floor) for floor in state[:-1]]
    floors = [floor if floor else '_'
              for floor in floors]
    floors = '|'.join(floors)
    elevator = state[-1]
    representation = '{}    {}'.format(elevator, floors)
    return representation


def path_repr(path):
    return [state_repr(state) for state in path]


def main():
    # # Example
    start = (
        ('HM', 'LM'),
        ('HG', ),
        ('LG', ),
        tuple(),
        0
    )

    paths = shortest_path(start, successors, heuristic)

    # # Input file
    start = (
        ('SG', 'SM', 'PG', 'PM'),
        ('TG', 'RG', 'RM', 'CG', 'CM'),
        ('TM',),
        tuple(),
        0
    )

    paths = shortest_path(start, successors, heuristic)


    # # Part 2
    # start = (
    #     ('SG', 'SM', 'PG', 'PM', 'EG', 'EM', 'DG', 'DM'),
    #     ('TG', 'RG', 'RM', 'CG', 'CM'),
    #     ('TM',),
    #     tuple(),
    #     0
    # )
    #
    # paths = shortest_path(start, successors, heuristic)


if __name__ == '__main__':
    main()
