import random
from copy import copy


class Card:
    SUIT_DICT = {
        'H': '♥',
        'D': '♦',
        'C': '♣',
        'S': '♠',
    }

    def __init__(self, rank_suit):
        rank_suit = rank_suit.strip()
        rank = rank_suit[:-1]
        suit = rank_suit[-1:]

        self.rank = rank.strip().upper()
        self.suit = suit.strip().upper()

    @classmethod
    def from_touple(cls, rank, suit):
        obj = cls.__new__(cls)  # Does not call __init__
        obj.rank = rank.strip().upper()
        obj.suit = suit.strip().upper()
        return obj

    def __repr__(self):
        return '{:>2}{}'.format(self.rank, self.SUIT_DICT[self.suit])

    def rank_value(self):
        ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
        return ranks.index(self.rank) + 2


def create_deck():
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    suits = 'H D C S'.split()

    return [Card.from_touple(r, s) for r in ranks for s in suits]


def deal(num_hands, cards_per_hand=5, deck=None):
    deck = copy(deck) if deck else create_deck()
    random.shuffle(deck)
    hands = []
    for i in range(num_hands):
        hand = [deck.pop() for j in range(cards_per_hand)]
        hands.append(hand)
    return hands
