class Solution:
    def compress(self, chars: list[str]) -> int:
        # if len(chars) == 0:
        #     return 0

        # temp = []

        # count = 1

        # for n in range(len(chars) - 1):
        #     if chars[n] == chars[n + 1]:
        #         count += 1
        #     else:
        #         temp.append(chars[n])
        #         if count != 1:
        #             temp2 = list(str(count))
        #             temp.extend(temp2)
        #             count = 1

        # temp.append(chars[len(chars) - 1])
        # if count != 1:
        #     temp2 = list(str(count))
        #     temp.extend(temp2)

        # for n in range(len(temp)):
        #     chars[n] = temp[n]

        # return len(temp)

        # Alternate solution by https://leetcode.com/singhabhinash/
        # Two pointers solution

        charsLength = len(chars)

        if charsLength == 1:
            return 1

        iteratingPointer = 0
        assignmentPointer = 0

        while iteratingPointer < charsLength:
            count = 1

            while iteratingPointer < charsLength - 1 and chars[iteratingPointer] == chars[iteratingPointer + 1]:
                count += 1
                iteratingPointer += 1

            chars[assignmentPointer] = chars[iteratingPointer]
            assignmentPointer += 1

            if count > 1:
                for countChar in str(count):
                    chars[assignmentPointer] = countChar
                    assignmentPointer += 1

            iteratingPointer += 1

        return assignmentPointer
