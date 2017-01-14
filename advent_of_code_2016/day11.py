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

import collections
import itertools


def partition(sequence, partition_length):
    sequence_length = len(sequence)
    return [tuple(sequence[i:i + partition_length])
            for i in range(0, sequence_length, partition_length)]


def parse(state_input):
    floors = [floor.split(',') if floor else []
              for floor in state_input]
    elevator = 0

    state = collections.defaultdict(dict)
    for floor_nr, floor in enumerate(floors):
        for item in floor:
            element, kind = item
            state[element][kind] = floor_nr

    state_list = [(value['G'], value['M'])
                  for value in state.values()]
    state_list.sort()

    state_representation = tuple(state_list), elevator

    return state_representation


def is_valid_floor(state, elevator):
    floor_elements = [(gen, chip)
                      for gen, chip in state[0]
                      if gen == elevator or chip == elevator]

    if not floor_elements:
        return True

    floor_unpaired_chips = [chip
                            for gen, chip in floor_elements
                            if chip == elevator and gen != elevator]
    floor_generators = [gen
                        for gen, chip in floor_elements
                        if gen == elevator]
    if floor_unpaired_chips and floor_generators:
        return False
    return True


def is_valid(state, old_elevator, new_elevator):
    return is_valid_floor(state, old_elevator) and is_valid_floor(state,
                                                                  new_elevator)


def successors(state):
    successors = set()
    elements, elevator = state
    elements_flat = [floor_nr
                     for element in elements
                     for floor_nr in element]

    current_floor_indexes = [idx
                             for idx, floor_nr in enumerate(elements_flat)
                             if floor_nr == elevator]

    index_groups = list(itertools.combinations(current_floor_indexes, 2))
    index_groups += list(itertools.combinations(current_floor_indexes, 1))

    next_elevator_floors = [elevator + delta
                            for delta in [-1, 1]
                            if 0 <= elevator + delta < 4]

    for next_elevator in next_elevator_floors:
        for indexes in index_groups:
            next_flat = elements_flat.copy()
            for index in indexes:
                next_flat[index] = next_elevator

            new_elements = partition(next_flat, 2)
            new_elements.sort()
            next_state = tuple(new_elements), next_elevator

            if next_state not in successors:
                if is_valid(next_state, elevator, next_elevator):
                    successors.add(next_state)

    return successors


def is_goal(state):
    elements, elevator = state
    items_on_lower_floors = any(item != (3, 3)
                                for item in elements)
    if items_on_lower_floors:
        return False
    return True


def shortest_path(start, successors, is_goal):
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        current_state = path[-1]
        for cell in successors(current_state):
            new_path = path + [cell]
            if is_goal(cell):
                # print()
                # print(len(new_path) - 1, len(explored))
                # pprint(new_path)
                return new_path
            elif cell not in explored:
                explored.add(cell)
                frontier.append(new_path)
    return []


def get_length(path):
    return len(path) - 1


def main():
    # Example
    example_input = ('HM,LM',
                     'HG',
                     'LG',
                     '')

    start = parse(example_input)
    path = shortest_path(start, successors, is_goal)
    print('Length example:', get_length(path))

    # Part 1
    part1_input = ('SG,SM,PG,PM',
                   'TG,RG,RM,CG,CM',
                   'TM',
                   '')

    start_part1 = parse(part1_input)
    path_part1 = shortest_path(start_part1, successors, is_goal)
    print('Length part one:', get_length(path_part1))

    # Part 2
    part2_input = ('SG,SM,PG,PM,EG,EM,DG,DM',
                   'TG,RG,RM,CG,CM',
                   'TM',
                   '')

    start_part2 = parse(part2_input)
    path_part2 = shortest_path(start_part2, successors, is_goal)
    print('Length part two:', get_length(path_part2))


if __name__ == '__main__':
    main()
