"""
--- Day 13: A Maze of Twisty Little Cubicles ---

You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward positive x and y; negative values are invalid, as they represent a location outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

Find x*x + 3*x + 2*x*y + y + y*y.
Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum; count the number of bits that are 1.
If the number of bits that are 1 is even, it's an open space.
If the number of bits that are 1 is odd, it's a wall.
For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as ., the corner of the building containing 0,0 would look like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###
Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###
Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

Your puzzle input is 1362.

"""
def is_odd(number):
  return number % 2 == 1


class Cell:
  puzzle_input = 1362

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def is_wall(self):
    decimal = (self.x * self.x + 3 * self.x + 2 * self.x * self.y + 
               self.y + self.y * self.y)
    decimal += self.puzzle_input
    binary = '{0:b}'.format(decimal)
    ones = binary.count('1')
    return is_odd(ones)

  def __str__(self):
    return '#' if self.is_wall() else '.'


def main():
  Cell.puzzle_input = 10
  for y in range(7):
    for x in range(10):
      print(Cell(x,y), end='')
    print()

if __name__ == '__main__':
  main()