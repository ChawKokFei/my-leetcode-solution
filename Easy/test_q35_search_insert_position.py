import unittest
from q35_search_insert_position import Solution


class Test35(unittest.TestCase):
    def test_searchInsert(self):
        self.assertEqual(Solution.searchInsert(self, [1, 4, 5, 7], 2), 1)
        self.assertEqual(Solution.searchInsert(self, [1, 4, 5, 7], 0), 0)
        self.assertEqual(Solution.searchInsert(self, [1, 4, 5, 7], 6), 3)
        self.assertEqual(Solution.searchInsert(self, [1, 4, 5, 7], 8), 4)
