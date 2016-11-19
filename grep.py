#! /usr/bin/env python3

"""
grep.py unix grep-like utility

Usage: grep.py PATTERN FILE

"""
import re
import sys

from utils import find_files


def grep_file(filename, search_regex):
    with open(filename, 'r') as f:
        for line_nr, line in enumerate(f.readlines()):
            if search_regex.search(line):
                print('{}:{}:{}'.format(filename, line_nr+1, line.strip()))


def main():
    search_pattern = sys.argv[1]
    search_regex = re.compile(search_pattern)
    shell_file_pattern = sys.argv[2]

    files = find_files('.', shell_pattern=shell_file_pattern)
    for filename in files:
        grep_file(filename, search_regex)


if __name__ == '__main__':
    main()
