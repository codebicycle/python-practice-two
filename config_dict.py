"""Read / write config file utilising the dict interface

"""
from pprint import pprint

class ConfigDict(dict):

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as f:
            for line in f:
                key, value = line.split('=')
                value = value.strip()
                dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self.filepath, 'w') as f:
            it = ('{}={}\n'.format(key, value) for key, value in self.items())
            f.writelines(it)


def main():
    cc = ConfigDict('config_file.txt')
    pprint(cc)

    cc['database'] = 'mysql_managed'       # [ this writes to the config file ]
    print('\nAfter assignment:')
    pprint(cc)


if __name__ == '__main__':
    main()
