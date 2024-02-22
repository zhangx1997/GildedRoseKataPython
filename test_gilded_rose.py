# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_vest_item_should_decrease_after_one_day(self):

        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]

    def test_vest_item_past_sellin_degrade_doubles(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 0, 19), Item(vest, 0, 19), Item(vest, 5, 8)]
        gr = GildedRose(items)

        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, -1, 17), Item(vest, -1, 17), Item(vest, 4, 7)]

        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, -2, 15), Item(vest, -2, 15), Item(vest, 3, 6)]

        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, -3, 13), Item(vest, -3, 13), Item(vest, 2, 5)]

    def test_sulfuras_item(self):
        pass

    def test_brie_item(self):
        pass

    def test_backstage_pass_item(self):
        pass

    def test_conjured_item_degrades_twice_as_fast(self):
        # Arrange
        cnj = "Conjured Mana Cake"
        items = [Item(cnj, 5, 42)]
        gr = GildedRose(items)

        items_cnj = gr.get_items_by_name(cnj)
        for item in items_cnj:
            original_sell_in = item.sell_in
            original_quality = item.quality

            # Act
            gr.update_quality()

            # Assert
            new_sell_in = item.sell_in
            new_quality = item.quality

            assert new_sell_in < original_sell_in
            assert original_sell_in - new_sell_in == 1

            validate_quality(new_quality)

            assert new_quality < original_quality
            assert original_quality - new_quality == 2

if __name__ == '__main__':
    unittest.main()
