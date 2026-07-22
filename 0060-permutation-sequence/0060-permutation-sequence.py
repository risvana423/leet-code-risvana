class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        nums = [str(i) for i in range(1, n+1)]
        k -= 1
        res = []
        for i in range(n, 0, -1):
            idx = k // math.factorial(i-1)
            res.append(nums.pop(idx))
            k %= math.factorial(i-1)
        return ''.join(res)

        