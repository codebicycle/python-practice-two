from poker import *


def test_create_deck():
    deck = create_deck()
    assert isinstance(deck, list), 'Should return a list'
    assert 52 == len(deck), 'Standard deck should have 52 cards'
    assert len(deck) == len(set(deck)), 'Standard deck should have unique cards'


def test_deal():
    hands = deal(5)
    flatten = [card for hand in hands for card in hand]
    assert isinstance(hands, list)
    assert len(flatten) == len(set(flatten)), (
        'Should deal unique cards for the standard deck')


def test_card_equivalent_initializers():
    card1 = Card('2H')
    card2 = Card.from_tuple('2', 'H')
    assert repr(card1) == repr(card2), (
        "Equivalent initializers should give the same representation")


def test_card_rank_value():
    queen_of_spades = Card('QS')
    ace_of_diamonds = Card('AD')
    deuce_of_hearts = Card('2H')
    ten_of_clubs = Card('10C')

    assert 12 == queen_of_spades.rank_value()
    assert 14 == ace_of_diamonds.rank_value()
    assert 2 == deuce_of_hearts.rank_value()
    assert 10 == ten_of_clubs.rank_value()


def test_ranks():
    hand = build_hand('2H QS AD 10C 10H')
    result = ranks(hand)
    expect = [14, 12, 10, 10, 2]
    assert expect == result


def test_is_staight():
    not_straight = build_hand('2H QS AD 10C 10H')
    straight = build_hand('7H 8S 9D 10C JH')
    ace_low_straight = build_hand('2H 3S 4D 5C AH')
    ace_high_straight = build_hand('AH KS QD JC 10H')

    assert is_straight(not_straight) is False
    assert is_straight(straight) is True
    assert is_straight(ace_low_straight) is True
    assert is_straight(ace_high_straight) is True


def test_is_flush():
    not_flush = build_hand('2H QH AH 10H 10D')
    flush = build_hand('7H 8H 9H 10H JH')

    assert is_flush(not_flush) is False
    assert is_flush(flush) is True


def test_poker_rank():
    high_card = build_hand('10C 9D JH 2H KS')
    pair = build_hand('7C 10C 2C 10D JC')
    two_pairs = build_hand('5C 5D 2C JC JD')
    three_of_a_kind = build_hand('5C 5D 5H JC 9D')
    full_house = build_hand('5C 5D 5H JC JD')
    four_of_a_kind = build_hand('5C 5D 5H 5S JD')

    assert ((1, 1, 1, 1, 1), (13, 11, 10, 9, 2)) == poker_rank(high_card)
    assert ((2, 1, 1, 1), (10, 11, 7, 2)) == poker_rank(pair)
    assert ((2, 2, 1), (11, 5, 2)) == poker_rank(two_pairs)
    assert ((3, 1, 1), (5, 11, 9)) == poker_rank(three_of_a_kind)
    assert ((3, 2), (5, 11)) == poker_rank(full_house)
    assert ((4, 1), (5, 11)) == poker_rank(four_of_a_kind)


def test_ranking():
    high_card = build_hand('10C 9D JH 2H KS')
    pair = build_hand('7C 10C 2C 10D JC')
    two_pairs = build_hand('5C 5D 2C JC JD')
    three_of_a_kind = build_hand('5C 5D 5H JC 9D')
    straight = build_hand('2C 3H 4H 5D 6C')
    flush = build_hand('9D JD AD 2D 5D')
    full_house = build_hand('5C 5D 5H JC JD')
    four_of_a_kind = build_hand('5C 5D 5H 5S JD')
    straight_flush = build_hand('4C 5C 6C 7C 8C')
    straight_flush_ace_low = build_hand('AC 2C 3C 4C 5C')
    royal_flush = build_hand('AS QS KS 10S JS')

    assert HIGH_CARD == ranking(high_card)[0]
    assert PAIR == ranking(pair)[0]
    assert TWO_PAIRS == ranking(two_pairs)[0]
    assert THREE_OF_A_KIND == ranking(three_of_a_kind)[0]
    assert STRAIGHT == ranking(straight)[0]
    assert FLUSH == ranking(flush)[0]
    assert FULL_HOUSE == ranking(full_house)[0]
    assert FOUR_OF_A_KIND == ranking(four_of_a_kind)[0]
    assert STRAIGHT_FLUSH == ranking(straight_flush)[0]
    assert STRAIGHT_FLUSH == ranking(straight_flush_ace_low)[0]
    assert ROYAL_FLUSH == ranking(royal_flush)[0]
