"""
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves into a bit of trouble. A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several more sub-towers. At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
...then you would be able to recreate the structure of the towers that looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth
In this example, tknk is at the bottom of the tower (the bottom program), and is holding up ugml, padx, and fwft. Those programs are, in turn, holding up other programs; in this example, none of those programs are holding up any other programs, and are all the tops of their own towers. (The actual tower balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program?

--- Part Two ---
The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all of their energy trying to keep the tower balanced. Apparently, one program has the wrong weight, and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?

"""
from collections import Counter, deque
import re

REGEX = re.compile(r'(?P<parent>\w+) .*-> (?P<children>[\w, ]+)', re.VERBOSE)


def parents_children(lines):
    parents_set = set()
    children_set = set()

    for line in lines:
        match = REGEX.match(line)
        if not match:
          continue
        parent = match.group('parent')
        children = [name.strip() for name in match.group('children').split(',')]

        parents_set.add(parent)
        children_set.update(children)
    return parents_set, children_set


class Node:
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = int(weight)
        self.children = children or []
        self.total_weight = None

    def set_total_weight(self):
        if not self.children:
            self.total_weight = self.weight
            return

        for child in self.children:
            if not child.total_weight:
                child.set_total_weight()

        children_total_weights = [child.total_weight for child in self.children]
        self.total_weight = self.weight + sum(children_total_weights)


    def balanced_weight(self):
        if not self.children:
            return None

        children_total_weights = [child.total_weight for child in self.children]

        counter = Counter(children_total_weights)
        if len(counter) > 1:
            most_common_value, _ = counter.most_common()[0]
            least_common_value, _ = counter.most_common()[-1]

            index = children_total_weights.index(least_common_value)
            unbalanced_child = self.children[index]

            difference = most_common_value - least_common_value
            return unbalanced_child.weight + difference

    def __repr__(self):
        return f'{self.name} {self.weight} {self.total_weight} {self.children}'


class TreeBuilder:
    PATTERN = r'(\w+) \((\d+)\)(?: -> ([\w, ]+))?'

    def __init__(self):
        self.incomplete = {}
        self.parents = {}
        self.trees = {}

    def parse(self, lines):
        for line in lines:
            name, weight, children_names = self._parse_line(line)
            if children_names:
                self.incomplete[name] = Node(name, weight)
                self.parents[name] = children_names
            else:
                self.trees[name] = Node(name, weight)

    def _parse_line(self, line):
        match = re.match(self.PATTERN, line)
        name, weight, children_str = match.groups()
        children_names = [c.strip() for c in children_str.split(',')] if children_str else None
        return name, weight, children_names

    def build(self):
        while self.incomplete:
            _, current = self.incomplete.popitem()
            tree = self._build_node(current)
            self.trees[tree.name] = tree

        _, root = self.trees.popitem()
        return Tree(root)

    def _build_node(self, node):
        for child_name in self.parents[node.name]:
            if child_name in self.trees:
                child = self.trees.pop(child_name)
                node.children.append(child)
            else:
                child = self.incomplete.pop(child_name)
                tree = self._build_node(child)
                node.children.append(tree)
        return node


class Tree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return str(self.root)

    def traverse(self):
        bfs = []
        queue = deque()
        queue.append(self.root)
        while queue:
            current = queue.popleft()
            bfs.append(current)
            if current.children:
                queue.extend(current.children)
        return reversed(bfs)

    def balanced_weight(self):
        for node in self.traverse():
            weight = node.balanced_weight()
            if weight:
                return weight


def read_lines(filename):
    with open(filename) as f:
        lines = list(f)
    return lines

def main():
    lines = read_lines('input7.txt')
    parents, children = parents_children(lines)

    result = (parents - children).pop()
    print(f'Part 1 solution: {result}')

    tree_builder = TreeBuilder()
    tree_builder.parse(lines)
    tree = tree_builder.build()
    tree.root.set_total_weight()

    result = tree.balanced_weight()
    print(f'Part 2 solution: {result}')


if __name__ == '__main__':
    main()
