from insertion_sort import insertion_sort

def test_insertion_sort():
    collection = [5, 3, 2, 4, 1]
    assert insertion_sort(collection) == list(sorted(collection))

    collection = [3, 4, 2, 1]
    assert insertion_sort(collection) == list(sorted(collection))
