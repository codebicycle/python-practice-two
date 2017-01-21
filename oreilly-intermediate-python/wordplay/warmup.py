from pprint import pprint

import scrabble


def main():

    uu = [word
          for word in scrabble.wordlist
          if 'uu' in word]

    print("Words containing 'uu':")
    for word in uu:
        print(word)


if __name__ == '__main__':
    main()
