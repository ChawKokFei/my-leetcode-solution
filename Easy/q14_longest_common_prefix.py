class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Take the first string, then compare its substring
        # with the substring of other string elements
        # in the array while incrementing the length
        # of substring on each iteration
        for n in range(1, len(strs[0]) + 1):
            for m in range(1, len(strs)):
                if strs[0][:n] != strs[m][:n]:
                    return strs[0][:n - 1]

        return strs[0]

        # Alternate solution
        #
        # res = ""
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]
        #
        # return res
