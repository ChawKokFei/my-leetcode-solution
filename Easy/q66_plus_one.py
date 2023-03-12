class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = [str(n) for n in digits]
        b = int("".join(a)) + 1
        c = str(b)
        d = list(c)
        e = [int(n) for n in d]
        return e
