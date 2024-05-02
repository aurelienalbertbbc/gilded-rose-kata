# -*- coding: utf-8 -*-
import unittest


from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_generic_product_positive_quality(self):
        Item("generic product", 0, -1)
    def test_generic_product(self):
        generic_product = Item("generic product", 10, 10)
        items = [generic_product]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("generic product", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_generic_product_sell_in_passed(self):
        generic_product = Item("generic product", 0, 10)
        items = [generic_product]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("generic product", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_generic_product_no_negative_quality(self):
        generic_product = Item("generic product", 10, 0)
        items = [generic_product]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("generic product", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie(self):
        pass
    
    def test_backstage_passes(self):
        pass

    def test_sulfuras(self):
        pass

    def test_conjured(self):
        pass



        
if __name__ == '__main__':
    unittest.main()
