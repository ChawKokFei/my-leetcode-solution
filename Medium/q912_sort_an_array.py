class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.mergeSort(nums)

        return nums

    # merge sort
    # time complexity O(n log n)
    # space complexity O(n)
    def mergeSort(self, array: list[int]):
        if len(array) <= 1:
            return

        mid = len(array) // 2
        leftArray = array[:mid]
        rightArray = array[mid:]

        self.mergeSort(leftArray)
        self.mergeSort(rightArray)

        leftPointer = rightPointer = oriPointer = 0

        while leftPointer < len(leftArray) and rightPointer < len(rightArray):
            if leftArray[leftPointer] <= rightArray[rightPointer]:
                array[oriPointer] = leftArray[leftPointer]
                leftPointer += 1
                oriPointer += 1
            else:
                array[oriPointer] = rightArray[rightPointer]
                rightPointer += 1
                oriPointer += 1

        if leftPointer < len(leftArray):
            for num in leftArray[leftPointer:]:
                array[oriPointer] = num
                oriPointer += 1

        if rightPointer < len(rightArray):
            for num in rightArray[rightPointer:]:
                array[oriPointer] = num
                oriPointer += 1
