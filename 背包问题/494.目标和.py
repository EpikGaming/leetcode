class Solution:
    def findTargetSumWays(self, nums: list, target: int):
        neg = sum(nums) - target
        if neg < 0 or neg & 1:
            return 0
        neg >>= 1
        dp = [1] + [0] * neg
        for num in nums:
            for j in range(neg, num - 1, -1):
                dp[j] += dp[j - num]
                print(num, j)
                print(dp)
        return dp

s = Solution()
test = [3, 4, 7, 9]
print(s.findTargetSumWays(test, 3))