from gilded_rose import Item, GildedRose, make_item

def test_foo():
    items = [make_item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert 'foo' == items[0].name
