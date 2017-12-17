
class GildedRose(object):
    def __init__(self, items):
        self.factory = Factory()
        self.items = [self.factory(item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def __init__(self, item):
        super().__init__(item.name, item.sell_in, item.quality)

    def update(self):
        self._update_sell_in()
        self._update_quality()

    def _update_sell_in(self):
        self.sell_in -= 1

    def _update_quality(self):
        self.quality -= 1 if self.sell_in < 0 else 0
        self.quality -= 1

        self._limit_quality_bottom()

    def _limit_quality_bottom(self):
        if self.quality < 0:
            self.quality = 0

    def _limit_quality_top(self):
        if self.quality > 50:
            self.quality = 50


class BrieItem(NormalItem):
    def _update_quality(self):
        self.quality += 1 if self.sell_in < 0 else 0
        self.quality += 1

        self._limit_quality_top()


class BackstageItem(NormalItem):
    def _update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality += 3
        elif self.sell_in < 10:
            self.quality += 2
        else:
            self.quality += 1

        self._limit_quality_top()


class SulfurasItem(NormalItem):
    def _update_sell_in(self):
        pass

    def _update_quality(self):
        pass


class ConjuredItem(NormalItem):
    def _update_quality(self):
        self.quality -= 2 if self.sell_in < 0 else 0
        self.quality -= 2

        self._limit_quality_bottom()


class Factory:
    MAP = {
        'aged brie': BrieItem,
        'backstage pass': BackstageItem,
        'sulfuras': SulfurasItem,
        'conjured': ConjuredItem,
        'normal': NormalItem,
    }

    @classmethod
    def __call__(cls, item):
        name = item.name.lower()

        for prefix in cls.MAP:
            if name.startswith(prefix):
                return cls.MAP[prefix](item)
        return cls.MAP['normal'](item)
