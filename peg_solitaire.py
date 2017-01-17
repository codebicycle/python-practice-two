PEG = '●'
HOLE = '○'

class Board:
    def __init__(self, triangle_side, hole):
        """@triangle_side int
           @hole coordinate tuple(x, y)"""
        self.triangle_side = triangle_side
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

    def __str__(self):
        width = self.triangle_side + (self.triangle_side - 1)
        accumulator = []
        for floor in reversed(self.coordinates):
            row = [PEG if self.board[coord] is True else HOLE
                   for coord in floor]
            row_str = ' '.join(row)
            centered = '{row:^{width}}'.format(row=row_str, width=width)
            accumulator.append(centered)
        return '\n'.join(accumulator)



def main():
    board = Board(5, (4, 2))
    print(board)


if __name__ == '__main__':
    main()