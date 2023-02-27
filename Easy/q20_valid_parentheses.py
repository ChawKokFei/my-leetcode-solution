class Solution:
    def isValid(self, s: str) -> bool:
        # Uses stack to solve the problem
        # stack = []

        # for n in s:
        #     if n in ["(", "{", "["]:
        #         stack.append(n)
        #     elif n == ")":
        #         if len(stack) != 0 and stack[-1] == "(":
        #             stack.pop()
        #         else:
        #             return False
        #     elif n == "}":
        #         if len(stack) != 0 and stack[-1] == "{":
        #             stack.pop()
        #         else:
        #             return False
        #     elif n == "]":
        #         if len(stack) != 0 and stack[-1] == "[":
        #             stack.pop()
        #         else:
        #             return False

        # if len(stack) != 0:
        #     return False

        # return True

        # Alternate solution by https://leetcode.com/jkim1519/
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0


solution = Solution()
solution.isValid("()")
solution.isValid("()[]{}")
solution.isValid("(]")
