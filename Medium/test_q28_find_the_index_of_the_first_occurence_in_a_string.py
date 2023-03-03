import unittest
from q28_find_the_index_of_the_first_occurence_in_a_string import Solution


class Test28(unittest.TestCase):
    def test_strStr(self):
        self.assertEqual(Solution.strStr(self, "sadbutsad", "sad"), 0)
        self.assertEqual(Solution.strStr(self, "leetcode", "leeto"), -1)
