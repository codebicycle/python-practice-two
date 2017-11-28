# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_helper(item)

    def _update_helper(self, item):
        if item.name == "Aged Brie":
            increase_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            increase_quality(item)
            if item.sell_in <= 10:
                increase_quality(item)
            if item.sell_in <= 5:
                increase_quality(item)
        else:
            decrease_quality(item)

        decrease_sell_in(item)

        if item.sell_in < 0:
            if item.name == "Aged Brie":
                increase_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = 0
            else:
                decrease_quality(item)


def increase_quality(item):
    if item.quality < 50:
        item.quality += 1

def decrease_quality(item):
    if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
        item.quality -= 1

def decrease_sell_in(item):
    if item.name != "Sulfuras, Hand of Ragnaros":
        item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
