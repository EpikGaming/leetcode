class Solution:
    def getMaximumGenerated(self, n: int):
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + i % 2 * nums[i // 2 + 1]
        return nums

s = Solution()
print(s.getMaximumGenerated(9))