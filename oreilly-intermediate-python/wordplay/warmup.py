import string
from pprint import pprint

import scrabble


def words_with_all_vowels(wordlist):
    vowels = set('aeiou')
    words = [word
             for word in wordlist
             if vowels.issubset(set(word))]
    return words


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

    print()
    print('Words containing all vowels:')
    for word in words_with_all_vowels(scrabble.wordlist):
        print(word)

if __name__ == '__main__':
    main()
