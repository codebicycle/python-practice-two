import fnmatch
import os
import re


def find_files(start_folder, pattern='.*', shell_pattern=None):
    """Find all files matching a pattern, traversing the directory tree
    from a given root note.

    :param start_folder:
    :param pattern: regexp style pattern
    :param shell_pattern: shell style pattern
    :return: set of file paths
    """
    if shell_pattern:
        pattern = fnmatch.translate(shell_pattern)

    regex = re.compile(pattern)
    files = set()
    for dirpath, dirnames, filenames in os.walk(start_folder):
        for filename in filenames:
            if regex.match(filename):
                filepath = os.path.join(dirpath, filename)
                files.add(filepath)
    return files
