class Solution:
    def lastStoneWeightII(self, stones: list):
        c = sum(stones) >> 1
        dp = [0 for _ in range(c + 1)]
        for i in range(len(stones)):
            for j in range(c, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sum(stones) - dp[-1] - dp[-1]

s = Solution()
test = [1,1,1,1,1,8]
print(s.lastStoneWeightII(test))