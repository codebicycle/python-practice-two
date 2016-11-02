"""Read / write config file utilising the dict interface

"""
from pprint import pprint
import os

class ConfigDict(dict):

    def __init__(self, filepath):

        self._filepath = filepath
        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                for line in f:
                    line = line.strip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)


    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)
        self._write_current_dict_to_file()


    def __delitem__(self, key):

        dict.__delitem__(self, key)
        self._write_current_dict_to_file()


    def _write_current_dict_to_file(self):

        with open(self._filepath, 'w') as f:
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
