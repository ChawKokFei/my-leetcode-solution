class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # Binary search
        # Iterative method
        while low <= high:
            # // integer division
            mid = low + ((high - low) // 2)

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return low
