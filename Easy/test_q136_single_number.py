import unittest
from q136_single_number import Solution


class Test136(unittest.TestCase):
    def test_singleNumber(self):
        self.assertEqual(Solution.singleNumber(self, [2, 2, 1]), 1)
        self.assertEqual(Solution.singleNumber(self, [4, 1, 2, 1, 2]), 4)
        self.assertEqual(Solution.singleNumber(self, [1]), 1)
