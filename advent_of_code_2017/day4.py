"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

"""

def count_passphrases(puzzle_input):
    count = 0
    for row in puzzle_input:
        if is_valid(row):
            count += 1
    return count

def is_valid(row):
    return len(row) == len(set(row))

def read_input(filename):
    with open(filename) as f:
        puzzle_input = [[word for word in line.split()] 
                        for line in f]
    return puzzle_input

def main():
    puzzle_input = read_input('input4.txt')

    result = count_passphrases(puzzle_input)
    print(f'Part 1 solution: {result}')


if __name__ == '__main__':
    main()
