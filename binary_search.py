
def contains(collection, target):
    return target in collection

def bs_contains(sorted_collection, target):
    low = 0
    high = len(sorted_collection) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == sorted_collection[mid]:
            return True
        elif target < sorted_collection[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


def binary_search(sorted_collection, target):
    low = 0
    high = len(sorted_collection) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == sorted_collection[mid]:
            return mid
        elif target < sorted_collection[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
