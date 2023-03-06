class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # missingIntArr = []
        # checkingNum = 1
        # i = 0

        # while len(missingIntArr) < k and i < len(arr):
        #     if checkingNum != arr[i]:
        #         missingIntArr.append(checkingNum)
        #         checkingNum += 1
        #     else:
        #         checkingNum += 1
        #         i += 1

        # if len(missingIntArr) < k:
        #     k -= len(missingIntArr)

        #     for n in range(k):
        #         missingIntArr.append(checkingNum)
        #         checkingNum += 1

        # if len(missingIntArr) > 0:
        #     return missingIntArr[-1]
        # else:
        #     return -1

        # Alternate solution
        # Binary search
        # O(log n)
        low = 0
        high = len(arr) - 1

        # index pos
        # 0, 1, 2, 3, 4
        # supposed like this
        # 1, 2, 3, 4, 5
        # 2, 3, 4, 7, 11
        # number of missing numbers
        # 1, 1, 1, 3, 6
        # k is at valueOfMissingNumberAtK of missing num at index 3 + 2
        # missing num
        # 1, 5, 6, 7, 9
        # means the value of k is 7 + 2 = 9

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid - 1

        numberOfMissingNumbers = arr[low - 1] - low
        remainingMissingNumber = k - numberOfMissingNumbers
        valueOfMissingNumberAtK = arr[low - 1] + remainingMissingNumber

        return valueOfMissingNumberAtK


solution = Solution()
solution.findKthPositive([2, 3, 4, 7, 11], 5)
