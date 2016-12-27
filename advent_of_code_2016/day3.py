"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

"""

import itertools

FILENAME = 'input3.txt'


def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def read_vertical():
    """Generator, read three lines at a time from file"""
    with open(FILENAME, 'r') as f:
        while True:
            try:
                three_lines = list(itertools.islice(f, 3))
                if three_lines:
                    yield three_lines
                else:
                    break
            except StopIteration:
                break


def parse(row):
    return (int(x) for x in row.split())


def parse_multiline(three_lines):
    lines = [parse(line) for line in three_lines]
    triangles = zip(*lines)
    return triangles


def parse_vertical():
    triangles = []
    for three_lines in read_vertical():
        fresh_triangles = parse_multiline(three_lines)
        triangles.extend(fresh_triangles)
    return triangles


def parse_normal():
    triangles = []
    with open(FILENAME, 'r') as f:
        for line in f:
            triangle = parse(line)
            triangles.append(triangle)
    return triangles


def count_valid_triangles(triangles):
    valid_triangles = 0
    for triangle in triangles:
        if is_valid_triangle(*triangle):
            valid_triangles += 1
    return valid_triangles


def main():
    assert is_valid_triangle(5, 10, 25) is False

    triangles = parse_normal()
    valid_triangles = count_valid_triangles(triangles)
    print(valid_triangles)

    triangles = parse_vertical()
    valid_triangles = count_valid_triangles(triangles)
    print(valid_triangles)


if __name__ == '__main__':
    main()
