class Solution:
    def hammingWeight(self, n: int):
        res = 0
        while n != 0:
            res += 1
            n &= n - 1
        return res

s = Solution()
test = 0b10101
print(s.hammingWeight(test))