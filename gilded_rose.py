# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


def make_item(*args, **kwargs):
    name = kwargs['name'] if 'name' in kwargs else args[0]
    name = name.lower()

    if 'aged brie' in name:
        return AgedBrie(*args, **kwargs)
    elif 'backstage pass' in name:
        return BackstagePass(*args, **kwargs)
    elif 'sulfuras' in name:
        return Sulfuras(*args, **kwargs)
    else:
        return NormalItem(*args, **kwargs)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def update(self):
        self.update_sellin()
        self.update_quality()

    def update_sellin(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.sell_in < 0:
            self.quality -= 2
        else:
            self.quality -= 1

        self._validate_quality()

    def _validate_quality(self):
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50


class AgedBrie(NormalItem):
    def update_quality(self):
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1

        self._validate_quality()


class BackstagePass(NormalItem):
    def update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality += 3
        elif self.sell_in < 10:
            self.quality += 2
        else:
            self.quality += 1

        self._validate_quality()


class Sulfuras(NormalItem):
    def update_sellin(self):
        pass

    def update_quality(self):
        pass
