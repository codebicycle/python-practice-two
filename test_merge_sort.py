from merge_sort import merge_sort

def test_merge_sort():
    collection = [5, 3, 2, 4, 1]
    assert merge_sort(collection) == list(sorted(collection))

    collection = [3, 4, 2, 1]
    assert merge_sort(collection) == list(sorted(collection))
