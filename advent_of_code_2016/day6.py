import collections


def main():
    with open('input6.txt', 'r') as f:
        lines = f.read().splitlines()

    columns = zip(*lines)
    most_common = [collections.Counter(column).most_common(1)[0][0]
                   for column in columns]

    message = ''.join(most_common)
    print(message)


if __name__ == '__main__':
    main()
