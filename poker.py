import random
from copy import copy

ROYAL_FLUSH = 10
STRAIGHT_FLUSH = 9
FOUR_OF_A_KIND = 8
FULL_HOUSE = 7
FLUSH = 6
STRAIGHT = 5
THREE_OF_A_KIND = 4
TWO_PAIRS = 3
PAIR = 2
HIGH_CARD = 1


class Card:
    SUIT_DICT = {
        'H': '♥',
        'D': '♦',
        'C': '♣',
        'S': '♠',
    }
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'H D C S'.split()

    def __init__(self, rank_suit):
        rank_suit = rank_suit.strip()
        rank = rank_suit[:-1]
        suit = rank_suit[-1:]

        self.rank = rank.strip().upper()
        self.suit = suit.strip().upper()

    @classmethod
    def from_tuple(cls, rank, suit):
        obj = cls.__new__(cls)  # Does not call __init__
        obj.rank = rank.strip().upper()
        obj.suit = suit.strip().upper()
        return obj

    def __repr__(self):
        return '{:>2}{}'.format(self.rank, self.SUIT_DICT[self.suit])

    def rank_value(self):
        return self.RANKS.index(self.rank) + 2


def create_deck():
    ranks = Card.RANKS
    suits = Card.SUITS
    return [Card.from_tuple(r, s) for r in ranks for s in suits]


def deal(num_hands, cards_per_hand=5, deck=None):
    deck = copy(deck) if deck else create_deck()
    random.shuffle(deck)
    hands = []
    for i in range(num_hands):
        hand = [deck.pop() for j in range(cards_per_hand)]
        hands.append(hand)
    return hands


def ranks(hand):
    """Rank values sorted from highest to lowest"""
    rank_values = [card.rank_value() for card in hand]
    rank_values.sort(reverse=True)

    # Ace low straight
    if [14, 5, 4, 3, 2] == rank_values:
        return [5, 4, 3, 2, 1]

    return rank_values


def is_ace_high(hand):
    rank_values = ranks(hand)
    return 14 == rank_values[0]


def is_straight(hand):
    rank_values = ranks(hand)

    for i in range(1, len(rank_values)):
        current = rank_values[i]
        previous = rank_values[i - 1]
        if current != previous - 1:
            return False
    return True


def is_flush(hand):
    suits = {card.suit for card in hand}
    return len(suits) == 1


def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)


def is_royal_flush(hand):
    return is_straight_flush(hand) and is_ace_high(hand)


def poker_rank(hand):
    count = {}
    rank_values = ranks(hand)
    for value in rank_values:
        count[value] = count.get(value, 0) + 1

    frequencies = sorted(count.values(), reverse=True)
    frequencies = tuple(frequencies)

    card_ranks = sorted(count, key=(lambda k: (count[k], k)), reverse=True)
    card_ranks = tuple(card_ranks)

    return frequencies, card_ranks


def ranking(hand):
    hand_rank = poker_rank(hand)
    frequencies, _values = hand_rank
    return (
        ROYAL_FLUSH if is_royal_flush(hand) else
        STRAIGHT_FLUSH if is_straight_flush(hand) else
        FOUR_OF_A_KIND if (4, 1) == frequencies else
        FULL_HOUSE if (3, 2) == frequencies else
        FLUSH if is_flush(hand) else
        STRAIGHT if is_straight(hand) else
        THREE_OF_A_KIND if (3, 1, 1) == frequencies else
        TWO_PAIRS if (2, 2, 1) == frequencies else
        PAIR if (2, 1, 1, 1) == frequencies else
        HIGH_CARD), hand_rank


def build_hand(hand_str):
    """
    :param hand_str: '9H 2C AH 10D 4H'
    :return: list of Cards
    """
    return [Card(card_str) for card_str in hand_str.split()]
