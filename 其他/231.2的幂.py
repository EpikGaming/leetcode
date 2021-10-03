class Solution:
    def isPowerOfTwo(self, n: int):
        x = bin(n)
        return x.count('1') == 1 if n > 0 else False

    def isPowerOfTwo2(self, n: int):
        return n > 0 and n & (n - 1) == 0

s = Solution()
test = -16
print(s.isPowerOfTwo(test))