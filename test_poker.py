from poker import create_deck, deal, Card


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
    card2 = Card.from_touple('2', 'H')
    assert repr(card1) == repr(card2), (
        "Equivalent initializers should give the same representation")


def test_ranks():
    queen_of_spades = Card('QS')
    ace_of_diamonds = Card('AD')
    deuce_of_hearts = Card('2H')
    ten_of_clubs = Card('10C')

    assert 12 == queen_of_spades.rank_value()
    assert 14 == ace_of_diamonds.rank_value()
    assert 2 == deuce_of_hearts.rank_value()
    assert 10 == ten_of_clubs.rank_value()
