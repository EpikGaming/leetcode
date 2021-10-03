class Solution:
    def isPowerOfFour(self, n: int):
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1

s = Solution()
test = int(input())
print(s.isPowerOfFour(test))