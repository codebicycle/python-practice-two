def insertion_sort(collection):
    """sort the collection using the insertion sort algorithm.
    Return a new sorted list.
    """
    collection = collection.copy()
    for i in range(1, len(collection)):
        insert(collection, i, collection[i])
    return collection


def insert(collection, index, value):
    """Insert value into its propper sorted place.
    Modifies the collection in place.
    Notice that collection from beginning up to index is sorted.
    """
    current = index - 1
    while current >= 0 and value < collection[current]:
        collection[current + 1] = collection[current]
        current -= 1
    collection[current + 1] = value
