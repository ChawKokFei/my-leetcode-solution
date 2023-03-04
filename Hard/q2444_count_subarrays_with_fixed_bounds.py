class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        lastMinIndex, lastMaxIndex, lastInvalidIndex, count = -1, -1, -1, 0

        # Credit to https://leetcode.com/singhabhinash/
        # Time complexity O(n)
        #
        # Approach
        # minIndex records the index position of the nums value that
        # equals to minK and maxIndex equalsd to maxK
        #
        # lastInvalidIndex records the boundary of the subarray
        # since the subarray must contain both the minimum and maximum values,
        # if the min(minIndex, maxIndex) > lastInvalidIndex, there is a valid subarray
        # else there is no valid subarray
        #
        # the max() method is to make sure in the case of max(0, -1)
        # it will be resolved to 0
        #
        # the number of subarrays is counted backwards
        # for example this one [1, 3, 5, 2, 1, 6, 7, 5]
        # lets say if right now lastMinIndex = 0 and lastMaxIndex = 2
        # the next iteration would makes the lastMinIndex become 4
        # when computing the count, the subarrays to add are as follows
        # 1, 3, 5, 2, 1
        # 3, 5, 2, 1
        # 5, 2, 1
        # because the lastInvalidIndex is -1, everything starting from
        # the next index has to be included
        #
        # the same goes to [1, 1, 1, 1]
        # index 0 checked, count += 1
        # index 1 checked, both
        # 1, 1
        # 1 (at index 1)
        # added, count += 2
        # and so on
        for n in range(len(nums)):
            if nums[n] >= minK and nums[n] <= maxK:
                lastMinIndex = n if nums[n] == minK else lastMinIndex
                lastMaxIndex = n if nums[n] == maxK else lastMaxIndex

                count += max(0, min(lastMinIndex, lastMaxIndex) -
                             lastInvalidIndex)
            else:
                lastInvalidIndex = n
                lastMinIndex = -1
                lastMaxIndex = -1

        return count


solution = Solution()
solution.countSubarrays([1, 3, 5, 2, 7, 5], 1, 5)
solution.countSubarrays([1, 1, 1, 1], 1, 1)
solution.countSubarrays([35054, 398719, 945315, 945315, 820417, 945315, 35054,
                         945315, 171832, 945315, 35054, 109750, 790964, 441974, 552913], 35054, 945315)
solution.countSubarrays([978650, 978650, 978650, 68071, 52201, 68071, 186141, 978650, 978650,
                        267135, 68071, 717241, 242895, 68071, 582505, 978650, 68071, 68071], 68071, 978650)
