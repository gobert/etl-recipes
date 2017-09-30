import helpers
import unittest
from models import Matchable


class MatchableTest(unittest.TestCase):
    def fuzzy_match(self, left, right):
        return Matchable(left).fuzzy_match(right)

    def test_match_same_string(self):
        self.assertTrue(self.fuzzy_match("chilie", "chilie"))

    def test_match_singular_plural(self):
        self.assertTrue(self.fuzzy_match("chilie", "chillies"))

    def test_match_small_mispell(self):
        self.assertTrue(self.fuzzy_match("chilie", "chiliee"))

    def test_does_not_match_huge_mispell(self):
        self.assertFalse(self.fuzzy_match("chilie", "chilean"))


if __name__ == '__main__':
    unittest.main()
