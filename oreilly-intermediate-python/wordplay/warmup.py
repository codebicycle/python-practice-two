import string
from pprint import pprint

import scrabble


def main():

    uu = [word
          for word in scrabble.wordlist
          if 'uu' in word]

    print("Words containing 'uu':")
    for word in uu:
        print(word)

    # Letter that do not appear doubled in words
    letters = set(string.ascii_lowercase)
    for letter in letters.copy():
        for word in scrabble.wordlist:
            if letter + letter in word:
                letters.remove(letter)
                break

    print()
    print('Letters that do not appear doubled in words:')
    print(', '.join(letters))

if __name__ == '__main__':
    main()
