class Solution:
    def isPowerOfThree(self, n: int):
        while n > 1 and n % 3 == 0:
            n //= 3
        return n == 1

s = Solution()
print(s.isPowerOfThree(27))