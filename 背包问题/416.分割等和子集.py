class Solution:
    def canPartition(self, nums: list):
        if len(nums) < 2 or sum(nums) & 1:
            return False
        temp = sum(nums) >> 1
        dp = [1] + [0] * temp
        for num in nums:
            for j in range(temp, num - 1, -1):
                dp[j] += dp[j - num]
                print(dp)
        return dp[-1] >= 2

test = [1, 5, 11, 5]
s = Solution()
print(s.canPartition(test))