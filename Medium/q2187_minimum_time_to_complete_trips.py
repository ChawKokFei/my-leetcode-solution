class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        # Binary search for searching the best time
        left = 1
        right = min(time) * totalTrips

        while left <= right:
            mid = left + (right - left) // 2

            if sum(mid // n for n in time) >= totalTrips:
                right = mid - 1
            else:
                left = mid + 1

        return left
