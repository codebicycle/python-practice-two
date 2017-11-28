# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


def increase_quality(item):
    if item.quality < 50:
        item.quality += 1

def decrease_quality(item):
    if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
        item.quality -= 1

def decrease_sell_in(item):
    if item.name != "Sulfuras, Hand of Ragnaros":
        item.sell_in -= 1

def make_item(*args, **kwargs):
    name = kwargs['name'] if 'name' in kwargs else args[0]
    name = name.lower()

    if 'aged brie' in name:
        return AgedBrie(*args, **kwargs)
    return NormalItem(*args, **kwargs)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def update_quality(self):
        if self.name == "Backstage passes to a TAFKAL80ETC concert":
            increase_quality(self)
            if self.sell_in <= 10:
                increase_quality(self)
            if self.sell_in <= 5:
                increase_quality(self)
        else:
            decrease_quality(self)

        decrease_sell_in(self)

        if self.sell_in < 0:
            if self.name == "Backstage passes to a TAFKAL80ETC concert":
                self.quality = 0
            else:
                decrease_quality(self)


class AgedBrie(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1
