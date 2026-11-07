import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSort(unittest.TestCase):
    def _cart(self):
        cart = Cart()
        cart.add_digital_video_disc(DigitalVideoDisc("b", cost=3.0))
        cart.add_digital_video_disc(DigitalVideoDisc("A", cost=1.0))
        cart.add_digital_video_disc(DigitalVideoDisc("c", cost=2.0))
        return cart

    def test_sort_by_title(self):
        titles = [d.title for d in self._cart().sort_by_title()]
        self.assertEqual(titles, ["A", "b", "c"])

    def test_sort_by_cost(self):
        costs = [d.cost for d in self._cart().sort_by_cost()]
        self.assertEqual(costs, [1.0, 2.0, 3.0])


if __name__ == "__main__":
    unittest.main()
