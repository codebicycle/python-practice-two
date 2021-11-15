"""
find.py unix find-like utility

Usage: find.py DIRECTORY PATTERN

"""
import os
import subprocess

HERE = os.path.dirname(__file__)


def test_basic(tmpdir):
    tmpdir.chdir()
    tmpdir.join('one.txt').write(b'one\n', 'wb')
    tmpdir.join('two.txt').write(b'two\n', 'wb')
    tmpdir.join('not-a-text-file').write(b'12345678', 'wb')

    find_filepath = os.path.join(HERE, 'find.py')
    start_folder = '.'
    pattern = '*.txt'
    completed_process = subprocess.run(['python', find_filepath, start_folder, pattern],
                                       stdout=subprocess.PIPE)
    output = completed_process.stdout

    assert output
    assert b'one.txt' in output
    assert b'two.txt' in output
    assert b'not-a-text-file' not in output
