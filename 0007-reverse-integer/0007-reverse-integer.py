class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = int(str(x)[::-1])
        return rev * sign if -(2**31) <= rev * sign <= 2**31 - 1 else 0

        