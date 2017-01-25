
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_sell_in(item)
            self._update_quality(item)

    @staticmethod
    def _update_sell_in(item):
        if not item.name.lower().startswith('sulfuras'):
            item.sell_in -= 1

    @staticmethod
    def _update_quality(item):
        name = item.name.lower()
        if name == 'aged brie':
            if item.sell_in > 0:
                item.quality += 1
            else:
                item.quality += 2
        elif name.startswith('backstage pass'):
            if item.sell_in < 0:
                item.quality = 0
            elif item.sell_in < 5:
                item.quality += 3
            elif item.sell_in < 10:
                item.quality += 2
            else:
                item.quality += 1
        elif name.startswith('sulfuras'):
            pass
        else:
            if item.sell_in > 0:
                item.quality -= 1
            else:
                item.quality -= 2

        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50:
            if not name.startswith('sulfuras'):
                item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
