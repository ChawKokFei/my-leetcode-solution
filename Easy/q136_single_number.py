class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        def mergeSort(array):
            if (len(array) > 1):
                # integer division, remainder part dropped
                mid = len(array) // 2
                # the start and end concept is same as java
                # where the end index includes only the
                # elements before it and start index
                # includes the elements starting from
                # the index position
                leftArray = array[:mid]
                rightArray = array[mid:]

                # keeps dividing the array down to 1 element
                mergeSort(leftArray)
                mergeSort(rightArray)

                # initializing the index position
                leftIndex = rightIndex = oriIndex = 0

                # compare left and right array
                # then put the lower one into the combined array
                # if one of the array reached its end, exit loop
                while leftIndex < len(leftArray) and rightIndex < len(rightArray):
                    if (leftArray[leftIndex] > rightArray[rightIndex]):
                        array[oriIndex] = rightArray[rightIndex]
                        oriIndex += 1
                        rightIndex += 1
                    else:
                        array[oriIndex] = leftArray[leftIndex]
                        oriIndex += 1
                        leftIndex += 1

                # insert the remaining sorted elements into the
                # combined array
                while leftIndex < len(leftArray):
                    array[oriIndex] = leftArray[leftIndex]
                    oriIndex += 1
                    leftIndex += 1

                while rightIndex < len(rightArray):
                    array[oriIndex] = rightArray[rightIndex]
                    oriIndex += 1
                    rightIndex += 1

        mergeSort(nums)

        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]
