class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list, profit: list):
        mod = 10 ** 9 + 7
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            member, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < member:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - member][max(0, k - earn)]) % mod
        print(dp)
        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % mod

    def profitableSchemes2(self, n: int, minProfit: int, group: list, profit: list):
        mod = 10 ** 9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        i = 0
        for earn, member in zip(profit, group):
            print(earn, member)
            for j in range(n, member - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j - member][max(0, k - earn)]) % mod
                    print(dp)
        return dp

s = Solution()
print(s.profitableSchemes2(10, 5, [2, 3, 5], [6, 7, 8]))