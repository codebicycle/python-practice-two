"""Sort candidates, give priority to priority set

"""
def sort_priority(candidates, priority):

    def priority_helper(item):
        if item in priority:
            return (0, item)
        else:
            return (1, item)

    ordered = sorted(candidates, key=priority_helper)
    return ordered


def main():
    candidates = [9, 4, 2, 6, 7, 3, 5, 1, 8]
    priority   = {9, 1, 3}

    ordered = sort_priority(candidates, priority)
    print(ordered)


if __name__ == '__main__':
    main()
