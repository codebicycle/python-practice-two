import collections


def main():
    with open('input6.txt', 'r') as f:
        lines = f.read().splitlines()

    columns = zip(*lines)
    frequency_columns = [collections.Counter(column).most_common()
                         for column in columns]

    most_common = [lst[0] for lst in frequency_columns]
    most_common_elements = [tup[0] for tup in most_common]

    least_common = [lst[-1] for lst in frequency_columns]
    least_common_elements = [tup[0] for tup in least_common]

    first_message = ''.join(most_common_elements)
    print(first_message)

    second_message = ''.join(least_common_elements)
    print(second_message)


if __name__ == '__main__':
    main()
