class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        positionOfElementToCheck = 0
        numberList = []
        symbolValue = {"I": 1, "V": 5, "X": 10,
                       "L": 50, "C": 100, "D": 500, "M": 1000}

        # Converting individual symbol into their respective value
        # Linear search
        # Time complexity: best O(n), worst O(n^2)
        for letter in s:
            for symbol in symbolValue:
                if letter == symbol:
                    numberList.append(symbolValue[symbol])

        # The positionOfElementToCheck variable indicates the value in the array
        # that has yet to be checked and added into the total value
        for index, number in enumerate(numberList):
            if index == len(numberList) - 1:
                if index == positionOfElementToCheck:
                    value += number
            else:
                if number > numberList[index + 1]:
                    if positionOfElementToCheck == index:
                        value += number
                        positionOfElementToCheck = index + 1
                    else:
                        positionOfElementToCheck = index + 1
                elif number == numberList[index + 1]:
                    value += number
                    positionOfElementToCheck = index + 1
                else:
                    value += (numberList[index + 1] - number)
                    positionOfElementToCheck = index + 2

        return value


solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))
print(solution.romanToInt("DCXXI"))
