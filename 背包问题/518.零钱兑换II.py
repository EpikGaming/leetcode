class Solution:
    def coinsChange(self, amount: int, coins: list):
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp

s = Solution()
test = [2]
print(s.coinsChange(3, test))