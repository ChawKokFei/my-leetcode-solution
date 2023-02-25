class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for n in s:
            if n in ["(", "{", "["]:
                stack.append(n)
            elif n == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif n == "}":
                if len(stack) != 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif n == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        if len(stack) != 0:
            return False

        return True


solution = Solution()
solution.isValid("()")
solution.isValid("()[]{}")
solution.isValid("(]")
