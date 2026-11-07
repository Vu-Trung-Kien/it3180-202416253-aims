import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):
    def _cart_100(self):
        cart = Cart()
        cart.add_digital_video_disc(DigitalVideoDisc("A", cost=100.0))
        return cart

    def test_discount_20_percent(self):
        self.assertAlmostEqual(self._cart_100().total_cost_with_discount(20), 80.0)

    def test_invalid_percent(self):
        with self.assertRaises(ValueError):
            self._cart_100().total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
