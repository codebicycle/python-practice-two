#! /usr/bin/env python3

"""
find.py unix find-like utility

Usage: find.py DIRECTORY -name PATTERN

"""

import subprocess

subprocess.run(['find', '.', '-name', '*.txt'])
