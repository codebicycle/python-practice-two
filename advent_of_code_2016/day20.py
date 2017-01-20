"""
--- Day 20: Firewall Rules ---

You'd like to set up a small hidden computer here so you can use it to get back into the network later. However, the corporate firewall only allows communication with certain external IP addresses.

You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in dot-decimal notation, they are written as plain 32-bit integers, which can have any value from 0 through 4294967295, inclusive.

For example, suppose only the values 0 through 9 were valid, and that you retrieved the following blacklist:

5-8
0-2
4-7

The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are not allowed. Then, the only IPs that this firewall allows are 3 and 9, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?

--- Part Two ---

How many IPs are allowed by the blacklist?

"""
import re

RE = re.compile(r'(\d+)-(\d+)')


def parse(lines):
    intervals = []
    for line in lines:
        match = RE.match(line)
        assert match
        start = int(match.group(1))
        end = int(match.group(2))
        intervals.append((start, end))

    return intervals


def group_intervals(intervals):
    ordered_intervals = sorted(intervals)
    accumulator = []

    previous_start, previous_end = ordered_intervals[0]
    for start, end in ordered_intervals:
        if start <= previous_end + 1:
            if end > previous_end:
                previous_end = end
        else:
            accumulator.append((previous_start, previous_end))
            previous_start, previous_end = start, end

    if accumulator[-1] != (previous_start, previous_end):
        accumulator.append((previous_start, previous_end))

    return accumulator


def find_lowest_ip(intervals):
    first_interval_start, first_interval_end = intervals[0]
    if first_interval_start != 0:
        lowest = 0
    else:
        lowest = first_interval_end + 1

    return lowest


def count_allowed_ips(intervals, max_limit):
    previous_start, previous_end = intervals[0]
    counter = previous_start - 0

    for start, end in intervals[1:]:
        if start >= max_limit:
            counter += max_limit - (previous_end + 1)
            break

        counter += start - (previous_end + 1)

        if end >= max_limit:
            break

        previous_start, previous_end = start, end
    return counter


def main():
    with open('input20.txt', 'r') as f:
        lines = f.readlines()

    raw_intervals = parse(lines)
    intervals = group_intervals(raw_intervals)

    lowest = find_lowest_ip(intervals)
    print('Lowest-valued IP is', lowest)

    max_limit = 4294967295
    allowed = count_allowed_ips(intervals, max_limit)
    print(allowed, 'allowed IPs')


if __name__ == '__main__':
    main()
