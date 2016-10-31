"""Python Beyond The Basics - Object Oriented Programming - Assignment 1

Create a simple class, MaxSizeList, that acts a little bit like a list, with a pre-configured limit on its size.  

Here some test calling code that imports the completed MaxSizeList and then uses it to create two new MaxSizeList objects.  


[calling code]

from assignments import MaxSizeList  # assumes "class MaxSizeList"
                                     # is in a script called "assignments.py"

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())

# ['hi', "let's", 'go']
# ['go']

"""

class MaxSizeList:

    def __init__(self, max_size):
        self.list     = []
        self.max_size = max_size

    def push(self, item):
        self.list.append(item)
        if len(self.list) > self.max_size:
            self.list.pop(0)

    def get_list(self):
        return self.list


def main():
    a = MaxSizeList(3)
    b = MaxSizeList(1)

    a.push("hey")
    a.push("hi")
    a.push("let's")
    a.push("go")

    b.push("hey")
    b.push("hi")
    b.push("let's")
    b.push("go")

    print(a.get_list())
    print(b.get_list())

if __name__ == '__main__':
    main()
