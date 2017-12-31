def merge_sort(collection):
    """Sort the collection using the merge sort algorithm.
    Return a new list.
    """
    if len(collection) < 2:
        return collection

    mid = len(collection) // 2
    left = merge_sort(collection[:mid])
    right = merge_sort(collection[mid:])

    ordered = []
    i = 0
    j = 0

    while True:
        if left[i] <= right[j]:
            ordered.append(left[i])
            i += 1
        else:
            ordered.append(right[j])
            j += 1

        if i >= len(left):
            ordered.extend(right[j:])
            break
        elif j >= len(right):
            ordered.extend(left[i:])
            break
    return ordered
