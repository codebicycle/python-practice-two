
def pairs_that_sum(numbers, total):
    """Given an integer array, 
    output all pairs that sum up to a specific value k.
    O(n log(n)

    """
    accumulator = []
    sorted_numbers = sorted(numbers)
    low = 0
    high = len(sorted_numbers) - 1

    while low < high:
        current_total = sorted_numbers[low] + sorted_numbers[high]

        if current_total == total:
            pair = sorted_numbers[low], sorted_numbers[high]
            accumulator.append(pair)
            low += 1
        elif current_total < total:
            low += 1
        else:
            high -= 1

    return sorted(set(accumulator))


def pairs_that_sum(numbers, total):
    """Given an integer array, 
    output all pairs that sum up to a specific value k.
    O(n)

    """
    accumulator = []
    seen = set()
    for num in numbers:
        required = total - num
        if required in seen:
            pair = tuple(sorted([num, required]))
            accumulator.append(pair)
            seen.remove(required)
        else:
            seen.add(num)

    return sorted(set(accumulator))
