import unittest
from unittest import TestCase

from shopping_cart import ShoppingCart


# write your tests here


class TestShoppingCart(TestCase):

    def setUp(self):
        self.cart = ShoppingCart(20)
        self.cart.add_item("potato", 200, 2)
        self.cart.add_item("tomato", 350, 1)
        self.cart.add_item("onion", 150, 1)

    def tearDown(self):
        del self.cart

    def test_add(self):
        self.cart.add_item("eggplant", 400, 1)
        self.assertEqual(self.cart.items,
                         [("potato", 200), ("potato", 200), ("tomato", 350), ("onion", 150), ("eggplant", 400)])
        self.assertEqual(self.cart.total, 1300)
        self.assertEqual(self.cart.item_count, 5)

    def test_remove(self):
        # self.cart.add_item("potato", 200, 2)
        removed = self.cart.remove_item("potato")
        self.assertEqual(self.cart.items, [("tomato", 350), ("onion", 150)])
        self.assertEqual(self.cart.total, 500)
        self.assertEqual(self.cart.item_count, 2)
        self.assertEqual(removed, [("potato", 200), ("potato", 200)])

    def test_mean(self):
        self.assertEqual(self.cart.mean_item_price(), 225)

    def test_median(self):
        self.assertEqual(self.cart.median_item_price(), 200)
        self.cart.add_item("eggplant", 400, 1)
        self.assertEqual(self.cart.median_item_price(), 200)

    def test_apply_discount(self):
        self.assertEqual(self.cart.apply_discount(), 720)
        self.assertEqual(self.cart.total, 720)

    def test_pop(self):
        self.assertEqual(self.cart.void_last_item(), ("onion", 150))
        self.assertEqual(self.cart.total, 750)
        self.assertEqual(self.cart.item_count, 3)


if __name__ == "__main__":
    unittest.main()
