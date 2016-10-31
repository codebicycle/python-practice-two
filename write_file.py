"""Python Beyond The Basics - Object Oriented Programming - Assignment 2

Create a very simple inheritance hierarchy of three classes that write to text files.  

LogFile(WriteFile):  its instance writes a date and message to a log file:  

2015-01-21 18:35   this is a log message


DelimFile (WriteFile):  its instance writes values separated by a delimeter:   

a,b,c,d


WriteFile(object):  the parent class to both LogFile and DelimFile, does work that is common between them.   Not intended to be instantiated.  


Here is calling code you can use to test:  

log = LogFile('log.txt')                  # passes the filename to write to
mydelim = DelimFile('data.csv', ',')      # passes the filename to write to
                                          # and a delimeter

log.write('this is a log message')        # writes a message to the file
log.write('this is another log message')  # same

mydelim.write(['a', 'b', 'c', 'd'])       # writes a list of values separated
                                          # by comma to the file
mydelim.write(['1', '2', '3', '4'])       # same


Here's what the two files look like when we're done:

# text of log.txt
2015-01-21 18:35   this is a log message
2015-01-21 18:35   this is another log message

# text of data.csv
a,b,c,d
1,2,3,4

"""
from datetime import datetime

class WriteFile:
    # TODO abstract class
    def __init__(self, filename):
        self.filename = filename


class LogFile(WriteFile):

    def write(self, message):
        with open(self.filename, 'a') as f:
            now = datetime.now()
            f.write("{:%Y-%m-%d %H:%M}\t{}\n".format(now, message))


class DelimFile(WriteFile):

    def __init__(self, filename, delimiter):
        super(DelimFile, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, values):
        values = list(map(
            (lambda val: '"{}"'.format(val) if self.delimiter in val else val),
            values))

        with open(self.filename, 'a') as f:
            line = self.delimiter.join(values)
            f.write("{}\n".format(line))


def main():
    log     = LogFile('tmp/log.txt')
    mydelim = DelimFile('tmp/data.csv', ',')

    log.write('this is a log message')
    log.write('this is another log message')
    mydelim.write(['a', 'b', 'c', 'd'])
    mydelim.write(['1', '2', '3', '4'])
    mydelim.write(['a', 'this, that', 'c', 'd'])


if __name__ == '__main__':
    main()
