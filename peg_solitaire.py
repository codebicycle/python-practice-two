"""
Peg Solitaire

Brute force solve for triangle board.

Initial board example:
    ●
   ● ●
  ● ○ ●
 ● ● ● ●
● ● ● ● ●

Example move:
    ●
   ● ●
  ● ◒ ●
 ● ● ○ ●
● ● ● ◌ ●

"""

import copy

PEG = '●'
HOLE = '○'
PREV_PEG = '◒'
PREV_HOLE = '◌'


def avg(*args):
    length = len(args)
    return sum(args) // length


class Board:
    def __init__(self, triangle_side, hole):
        """@triangle_side int
           @hole coordinate tuple(x, y)"""

        self.triangle_side = triangle_side
        self.n = (self.triangle_side + 1) * self.triangle_side / 2
        self.path = []
        self.board = {}
        self.coordinates = []

        for y in range(self.triangle_side):
            row = []
            for x in range(self.triangle_side - y):
                coord = (x*2+y, y) 
                self.board[coord] = True
                row.append(coord)
            self.coordinates.append(row)

        self.board[hole] = False
        self.initial_board = copy.deepcopy(self.board)

    def __str__(self):
        width = self.triangle_side + (self.triangle_side - 1)

        previous_move = self.path[-1] if self.path else None
        prev_start = previous_move[0] if previous_move else None
        prev_end = previous_move[1] if previous_move else None

        accumulator = []
        for row in reversed(self.coordinates):
            symbol_row = []
            for coord in row:
                if self.board[coord] is True:
                    symbol = PREV_PEG if coord == prev_end else PEG
                else:
                    symbol = PREV_HOLE if coord == prev_start else HOLE
                symbol_row.append(symbol)

            row_str = ' '.join(symbol_row)
            centered = '{row:^{width}}'.format(row=row_str, width=width)
            accumulator.append(centered)
        return '\n'.join(accumulator)

    def make_move(self, move):
        """@move (start, end); start , end coordinates"""
        start, end = move
        middle = (avg(start[0], end[0]), avg(start[1], end[1]))
        self.board[start] = False
        self.board[middle] = False
        self.board[end] = True

    def undo_move(self, move):
        """@move (start, end); start , end coordinates"""
        start, end = move
        middle = (avg(start[0], end[0]), avg(start[1], end[1]))
        self.board[end] = False
        self.board[middle] = True
        self.board[start] = True

    def available_moves(self):
        moves = []
        directions = ((4, 0), (-4, 0), (2, 2), (-2, -2), (2, -2), (-2, 2))
        for coord in self.board:
            start = coord
            if self.board[start] is False:
                continue
            for delta in directions:
                end = coord[0] + delta[0], coord[1] + delta[1]
                if end not in self.board or self.board[end] is True:
                    continue
                middle = (avg(start[0], end[0]), avg(start[1], end[1]))
                if self.board[middle] is True:
                    move = start, end
                    moves.append(move)
        return moves

    def is_solved(self):
        """After n-2 moves puzzle is solved """
        return len(self.path) == self.n - 2

    def solve(self):
        if self.is_solved():
            return True
        for move in self.available_moves():
            self.make_move(move)
            self.path.append(move)

            if self.solve() is True:
                return True

            self.undo_move(move)
            del self.path[-1]

        return False

    def print_steps(self):
        path_clone = self.path.copy()
        # reset
        self.board = copy.deepcopy(self.initial_board)
        self.path = []

        for move in path_clone:
            print(self)
            self.make_move(move)
            self.path.append(move)

        print(self)


def main():
    board = Board(5, (3, 1))
    board.solve()
    board.print_steps()


if __name__ == '__main__':
    main()
