from pprint import pprint

import math
import pytest

from gilded_rose import Item, GildedRose


@pytest.fixture
def gilded_rose():
    wolf3d_items = [
        Item(name='food', sell_in=10, quality=10),
        Item(name='dog food', sell_in=10, quality=4),
        Item(name='first aid kit', sell_in=10, quality=25),
        Item(name='Sulfuras', sell_in=math.inf, quality=80),
        Item(name='Aged Brie', sell_in=10, quality=15),
        Item(name='backstage passes to QuakeCon', sell_in=20, quality=10),
        Item(name='conjured crown', sell_in=20, quality=50),
    ]
    return GildedRose(wolf3d_items)


def days_after(days, gildedrose):
    print('After {} days'.format(days))
    for _ in range(days):
        gildedrose.update_quality()


@pytest.mark.xfail
def test_text(gilded_rose):
    pprint(gilded_rose.items)

    days_after(1, gilded_rose)
    pprint(gilded_rose.items)

    days_after(8, gilded_rose)
    pprint(gilded_rose.items)

    days_after(1, gilded_rose)
    pprint(gilded_rose.items)

    days_after(1, gilded_rose)
    pprint(gilded_rose.items)
    assert False


def test_decrease_sell_in(gilded_rose):
    initial_sell_ins = [item.sell_in for item in gilded_rose.items]
    gilded_rose.update_quality()
    for index, item in enumerate(gilded_rose.items):
        assert item.sell_in == initial_sell_ins[index] - 1


def test_quality_is_positive(gilded_rose):
    gilded_rose.update_quality()
    items_quality_positive = lambda: (item.quality >= 0
                                      for item in gilded_rose.items)
    assert all(items_quality_positive())

    days_after(500, gilded_rose)
    assert all(items_quality_positive())


def test_quality_is_limited_to_50(gilded_rose):
    gilded_rose.update_quality()
    items_quality_max = lambda: (item.quality <= 50
                                 for item in gilded_rose.items
                                 if not item.name.lower().startswith(
                                    'sulfuras'))
    assert all(items_quality_max())

    days_after(500, gilded_rose)
    assert all(items_quality_max())


def test_sulfuras(gilded_rose):
    items = [Item('Sulfuras', sell_in=math.inf, quality=80)]
    inventory = GildedRose(items)
    item = inventory.items[0]

    inventory.update_quality()
    assert 80 == item.quality
    assert math.inf == item.sell_in

    days_after(500, inventory)
    assert 80 == item.quality
    assert math.inf == item.sell_in


def test_aged_brie_increase_quality():
    quality = 10
    items = [Item('Aged Brie', sell_in=5, quality=quality)]
    inventory = GildedRose(items)
    item = inventory.items[0]

    quality += 1
    inventory.update_quality()
    assert quality == item.quality

    # after sell_in
    quality += 2
    item.sell_in = 0
    days_after(1, inventory)
    assert quality == item.quality


def test_quality_decrease():
    quality = 10
    items = [Item('food', sell_in=5, quality=quality)]
    inventory = GildedRose(items)
    item = inventory.items[0]

    inventory.update_quality()
    quality -= 1
    assert quality == item.quality

    inventory.update_quality()
    quality -= 1
    assert quality == item.quality


def test_quality_decrease_twice_after_sell_in():
    quality = 10
    items = [Item('food', sell_in=0, quality=quality)]
    inventory = GildedRose(items)
    item = inventory.items[0]

    inventory.update_quality()
    quality -= 2
    assert quality == item.quality

    inventory.update_quality()
    quality -= 2
    assert quality == item.quality


def test_backstage_pass():
    quality = 10
    items = [Item('backstage passes to QuakeCon', sell_in=20, quality=quality)]
    inventory = GildedRose(items)
    item = inventory.items[0]

    # more than 10 days remaining
    quality += 1
    inventory.update_quality()
    assert quality == item.quality

    # 10 days or less
    item.sell_in = 10
    quality += 2
    inventory.update_quality()
    assert quality == item.quality

    quality += 2
    inventory.update_quality()
    assert quality == item.quality

    # 5 days or less
    item.sell_in = 5
    quality += 3
    inventory.update_quality()
    assert quality == item.quality

    quality += 3
    inventory.update_quality()
    assert quality == item.quality

    item.sell_in = 1
    quality += 3
    inventory.update_quality()
    assert quality == item.quality

    # after sell_in date
    item.sell_in = 0
    inventory.update_quality()
    assert 0 == item.quality

    inventory.update_quality()
    assert 0 == item.quality
