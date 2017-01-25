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


def test_update_quality_decrease_sell_in(gilded_rose):
    initial_sell_ins = [item.sell_in for item in gilded_rose.items]
    gilded_rose.update_quality()
    for index, item in enumerate(gilded_rose.items):
        assert item.sell_in == initial_sell_ins[index] - 1
