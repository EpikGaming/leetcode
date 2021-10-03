class Solution:
    def combinationSum4(self, nums: list, target: int):
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for j in nums:
                if j <= i:
                    dp[i] += dp[i - j]
        return dp

    def coinsChange(self, coins: list, amount: int):
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp

test = [1, 2, 3]
s = Solution()
print(s.combinationSum4(test, 4))
print(s.coinsChange(test, 4))