# -*- coding: utf-8 -*-
import unittest


from gilded_rose import GildedRose, Item
from python.gilded_rose import SpecialProducts


class GildedRoseTest(unittest.TestCase):
    def setUpSingleItem(self, name: str = "generic product", sell_in: int = 10, quality: int = 10):
        generic_product = Item(name, sell_in, quality)
        return [generic_product]

    def test_generic_product(self):
        items = self.setUpSingleItem()
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("generic product", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_generic_product_sell_in_passed(self):
        items = self.setUpSingleItem(sell_in=0, quality=10)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("generic product", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_generic_product_no_negative_quality(self):
        items = self.setUpSingleItem(sell_in=10, quality=0)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("generic product", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie(self):
        items = self.setUpSingleItem(name=SpecialProducts.AGED_BRIE.value, sell_in=10, quality=0)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(SpecialProducts.AGED_BRIE.value, items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_max_quality(self):
        items = self.setUpSingleItem(name=SpecialProducts.AGED_BRIE.value, sell_in=10, quality=50)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(SpecialProducts.AGED_BRIE.value, items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_more_than_10_days(self):
        name = SpecialProducts.BACKSTAGE.value
        items = self.setUpSingleItem(name=name, sell_in=15, quality=0)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(name, items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_backstage_less_than_10_days(self):
        items = self.setUpSingleItem(name=SpecialProducts.BACKSTAGE.value, sell_in=10, quality=0)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(SpecialProducts.BACKSTAGE.value, items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_backstage_less_than_5_days(self):
        items = self.setUpSingleItem(name=SpecialProducts.BACKSTAGE.value, sell_in=4, quality=0)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(SpecialProducts.BACKSTAGE.value, items[0].name)
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_backstage_beyond_concert_date(self):
        name = SpecialProducts.BACKSTAGE.value
        items = self.setUpSingleItem(name=name, sell_in=0, quality=33)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(name, items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_below_50(self):
        name = SpecialProducts.BACKSTAGE.value
        items = self.setUpSingleItem(name=name, sell_in=4, quality=50)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(name, items[0].name)
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_does_not_change(self):
        name = SpecialProducts.SULFURAS.value
        items = self.setUpSingleItem(name=name, sell_in=4, quality=80)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(name, items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_conjured(self):
        pass



        
if __name__ == '__main__':
    unittest.main()
