import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title_exact_match(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        result = search_by_title(items, "Aladdin")
        self.assertEqual([d.title for d in result], ["Aladdin"])


if __name__ == "__main__":
    unittest.main()
