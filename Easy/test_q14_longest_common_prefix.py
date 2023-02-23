import unittest
from q14_longest_common_prefix import Solution

class Test14(unittest.TestCase):
    def test_longestCommonPrefix(self):
        self.assertEqual(Solution.longestCommonPrefix(self, ["flower", "flow", "flight"]), "fl")
        self.assertEqual(Solution.longestCommonPrefix(self, ["c", "acc", "cccc"]), "")
