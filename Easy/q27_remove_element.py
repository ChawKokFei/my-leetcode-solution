class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Two pointers technique
        # if len(nums) == 0:
        #     return 0

        # left = 0
        # right = len(nums) - 1

        # while left != right:
        #     if nums[left] == val:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         right -= 1
        #     else:
        #         left += 1

        # if nums[right] == val:
        #     return right
        # else:
        #     return right + 1

        # Alternate solution
        rHSOfNotVal = 0

        for num in nums:
            if num != val:
                nums[rHSOfNotVal], num = num, nums[rHSOfNotVal]
                rHSOfNotVal += 1

        return rHSOfNotVal
