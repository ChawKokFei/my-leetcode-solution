class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # nums.sort()
        # for n in range(len(nums) - 1):
        #     if nums[n] == nums[n+1]:
        #         return True
        # return False

        # Alternate solution
        # set which uses hash table
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)

        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
