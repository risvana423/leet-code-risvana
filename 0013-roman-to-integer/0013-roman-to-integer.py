class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res, prev = 0, 0
        for c in reversed(s):
            if values[c] < prev:
                res -= values[c]
            else:
                res += values[c]
            prev = values[c]
        return res

        