class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        print(needle, haystack)
        if needle not in haystack:
            return -1

        left = 0
        right = len(needle) - 1

        while right < len(haystack):
            if needle == haystack[left: right + 1]:
                return left
            left += 1
            right += 1

        return -1
