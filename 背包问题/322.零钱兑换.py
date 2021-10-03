class Solution:
    def coinChange(self, coins: list, amount: int):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
                print(dp)
        return dp

s = Solution()
test = [1,2,5]
print(s.coinChange(test, 11))