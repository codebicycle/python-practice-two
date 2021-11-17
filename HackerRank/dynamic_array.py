def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    answers = []
    for query in queries:
        type_, x, y = query
        idx = (x ^ last_answer) % n
        if type_ == 1:
            arr[idx].append(y)
        elif type_ == 2:
            idx2 = y % len(arr[idx])
            last_answer = arr[idx][idx2]
            answers.append(last_answer)
        else:
            raise ValueError(f'Unknown type {type_}')
    return tuple(answers)


if __name__ == '__main__':
    n = 2
    queries = [(1, 0, 5), (1, 1, 7), (1, 0, 3), (2, 1, 0), (2, 1, 1)]
    result = dynamicArray(n, queries)
    expected = (7, 3)
    assert result == expected
