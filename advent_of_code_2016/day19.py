"""
--- Day 19: An Elephant Named Joseph ---

The Elves contact you over a highly secure emergency channel. Back at the North Pole, the Elves are busy misunderstanding White Elephant parties.

Each Elf brings a present. They all sit in a circle, numbered starting with position 1. Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left. An Elf with no presents is removed from the circle and does not take turns.

For example, with five Elves (numbered 1 to 5):

  1
5   2
 4 3

    Elf 1 takes Elf 2's present.
    Elf 2 has no presents and is skipped.
    Elf 3 takes Elf 4's present.
    Elf 4 has no presents and is also skipped.
    Elf 5 takes Elf 1's two presents.
    Neither Elf 1 nor Elf 2 have any presents, so both are skipped.
    Elf 3 takes Elf 5's three presents.

So, with five Elves, the Elf that sits starting in position 3 gets all the presents.

With the number of Elves given in your puzzle input, which Elf gets all the presents?

Your puzzle input is 3005290.

"""


class Node:
    def __init__(self, index, next=None):
        self.index = index
        self.value = 1
        self.next = next

    def __repr__(self):
        return 'index {}, value {}'.format(self.index, self.value)


def create_elfs(number):
    elfs = [Node(i) for i in range(1, number + 1)]

    for idx in range(len(elfs) - 1):
        elfs[idx].next = elfs[idx + 1]
    elfs[-1].next = elfs[0]

    return elfs


def exchange_gifts(elfs):
    current = elfs[0]
    while current.index != current.next.index:
        successor = current.next

        current.value += successor.value
        current.next = successor.next

        current = current.next
    current.next = None

    return current.index


def main():
    puzzle_input = 3005290

    elfs = create_elfs(puzzle_input)
    lucky_elf_index = exchange_gifts(elfs)
    print(lucky_elf_index)

if __name__ == '__main__':
    main()
