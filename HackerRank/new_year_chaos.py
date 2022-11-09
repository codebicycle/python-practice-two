from collections import defaultdict


def minimum_bribes(q):
    """for each person in the final state of the queue
        count how many persons it bribed (values lower behind in the queue)
        If there are more than 2 bribed persons stop"""
    total_bribes = 0
    for i, person in enumerate(q):
        bribes = 0
        for next_in_line in q[i:]:
            if person > next_in_line:
                bribes += 1
                if bribes > 2:
                    return -1
        total_bribes += bribes
    return total_bribes


def minimum_bribes(q):
    """Optimize the count of bribed persons for each individual
    a bribed person has a lower value and is behind in the queue"""
    bribes = {}
    for person in reversed(q):
        bribed_list = [x for x in bribes if x < person]
        if len(bribed_list) > 2:
            return -1
        bribes[person] = bribed_list

    bribes_count = 0
    for bribed_list in bribes.values():
        count = len(bribed_list)
        if count > 2:
            return -1
        bribes_count += count
    return bribes_count


def minimum_bribes(q):
    """For each person in queue keep track of the missing persons"""
    total_bribes = 0
    missing = set()
    initial_queue = list(range(1, len(q) + 1))
    idx = 0
    for person in q:
        missing.discard(person)
        missing_current = initial_queue[idx: person - 1]
        missing = missing | set(missing_current)
        bribes = len(tuple(x for x in missing if x < person))
        if bribes > 2:
            return -1
        total_bribes += bribes
        idx = max(idx, person)
    return total_bribes


def minimum_bribes(q):
    """Swap sort"""
    size = len(q)
    if size < 2:
        return 0

    bribes_map = defaultdict(int)
    bribes = 0
    while True:
        swaps = 0
        i = 0
        j = 1
        while True:
            if q[i] > q[j]:
                q[i], q[j] = q[j], q[i]
                swaps += 1

                bribes_map[q[j]] += 1
                if bribes_map[q[j]] > 2:
                    return -1

            if j >= size-1:
                break
            i += 1
            j += 1

        bribes += swaps
        if swaps == 0:
            break

    return bribes



def minimumBribes(q):
    bribes = minimum_bribes(q)
    if bribes == -1:
        print('Too chaotic')
    else:
        print(bribes)


if __name__ == '__main__':
    q = [4, 1, 2, 3]
    result = minimum_bribes(q)
    assert result == -1

    q = [1, 2, 5, 3, 7, 8, 6, 4]
    # 1 2 3 4 5 6 7 8 start
    # 1 2 5 3 4 6 7 8 - 2
    # 1 2 5 3 6 4 7 8 - 1
    # 1 2 5 3 7 6 4 8 - 2
    # 1 2 5 3 7 8 6 4 - 2
    result = minimum_bribes(q)
    assert result == 7

    q = [2, 5, 1, 3, 4]
    result = minimum_bribes(q)
    assert result == -1
