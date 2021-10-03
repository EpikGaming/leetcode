class Solution:
    def minSteps(self, n: int):
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = float('inf')
            j = 1
            while j * j <= i:
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
                    dp[i] = min(dp[i], dp[i // j] + j)
                j += 1
        return dp


s = Solution()
print(s.minSteps(9))