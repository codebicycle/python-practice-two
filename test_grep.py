"""
grep.py unix grep-like utility

Usage: grep.py PATTERN FILE

"""
import os
import subprocess

HERE = os.path.dirname(__file__)


def test_basic(tmpdir):
    tmpdir.chdir()
    tmpdir.join('one.txt').write(b'one\n', 'wb')
    tmpdir.join('two.txt').write(b'two\n', 'wb')
    tmpdir.join('not-a-text-file').write(b'12345678', 'wb')

    grep_filepath = os.path.join(HERE, 'grep.py')
    completed_process = subprocess.run([grep_filepath, 'one', '*.txt'],
                                       stdout=subprocess.PIPE)
    output = completed_process.stdout

    assert output
    assert b'one.txt:1:one\n' in output
