import unittest
from q27_remove_element import Solution


class Test27(unittest.TestCase):
    def test_removeElement(self):
        self.assertEqual(Solution.removeElement(self, [3, 2, 2, 3], 3), 2)
        self.assertEqual(Solution.removeElement(
            self, [0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
