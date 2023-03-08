import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 0
        right = max(piles)

        while left < right:
            k = left + (right - left) // 2

            if k == 0:
                return 1

            if sum(math.ceil(n / k) for n in piles) > h:
                left = k + 1
            else:
                right = k

        return left


solution = Solution()
# solution.minEatingSpeed([30, 11, 23, 4, 20], 5)
# solution.minEatingSpeed([312884470], 968709470)
solution.minEatingSpeed([3, 6, 7, 11], 18)
