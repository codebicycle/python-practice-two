#! /usr/bin/env python3

"""
find.py unix find-like utility

Usage: find.py DIRECTORY -name PATTERN

"""
import os
import subprocess
import sys
from fnmatch import fnmatch

# subprocess.run(['find', '.', '-name', '*.txt'])


def main():
    start = sys.argv[1]
    pattern = sys.argv[3]

    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames:
            if fnmatch(filename, pattern):
                filepath = os.path.join(dirpath, filename)
                print(filepath)


if __name__ == '__main__':
    main()
