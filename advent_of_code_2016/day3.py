"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

"""


def parse(row):
    return (int(x) for x in row.split())


def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def main():
    assert is_valid_triangle(5, 10, 25) is False

    with open('input3.txt', 'r') as f:
        lines = f.readlines()

    valid_triangles = 0
    for line in lines:
        lengths = parse(line)
        if is_valid_triangle(*lengths):
            valid_triangles += 1

    print(valid_triangles)


if __name__ == '__main__':
    main()
