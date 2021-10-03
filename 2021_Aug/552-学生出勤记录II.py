class Solution:
    def checkRecord(self, n: int):
        MOD = 10 ** 9 + 7
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n + 1)]
        dp[0][0][0] = 1
        for i in range(1, n + 1):
            for j in range(0, 2):
                for k in range(0, 3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

            for k in range(0, 3):
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

            for j in range(0, 2):
                for k in range(1, 3):
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD
        res = 0
        for j in range(0, 2):
            for k in range(0, 3):
                res += dp[n][j][k]

        return dp, res % MOD

    def checkRecord2(self, n: int):
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(3)] for _ in range(2)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            newDP = [[0 for _ in range(3)] for _ in range(2)]

            for j in range(0, 2):
                for k in range(0, 3):
                    newDP[j][0] = (newDP[j][0] + dp[j][k]) % MOD

            for k in range(0, 3):
                newDP[1][0] = (newDP[1][0] + dp[0][k]) % MOD

            for j in range(0, 2):
                for k in range(1, 3):
                    newDP[j][k] = (newDP[j][k] + dp[j][k - 1]) % MOD
            dp = newDP

        res = 0
        for j in range(0, 2):
            for k in range(0, 3):
                res += dp[j][k]
        return dp, res % MOD

    def checkRecord3(self, n: int):
        MOD = 10 ** 9 + 7
        M = [[1, 1, 0, 1, 0, 0],
             [1, 0, 1, 1, 0, 0],
             [1, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 1]]

        def matrixMul(matrixA: list, matrixB: list):
            return [[sum(a * b for a, b in zip(m1, m2)) % MOD for m2 in zip(*matrixB)] for m1 in matrixA]

        res = [[1, 0, 0, 0, 0, 0]]
        while n:
            if n & 1:
                res = matrixMul(res, M)
            M = matrixMul(M, M)
            n >>= 1
        return sum(res[0]) % MOD


s = Solution()
print(s.checkRecord3(3))