class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list):
        dp = [0] * (n + 1)
        dp[1] = 1
        m = len(primes)
        pointer = [1] * m

        for i in range(2, n + 1):
            temp = min(dp[pointer[j]] * primes[j] for j in range(m))
            dp[i] = temp
            for j in range(m):
                if dp[pointer[j]] * primes[j] == temp:
                    pointer[j] += 1
        return dp

s = Solution()
test = [2, 7, 13, 19]
print(s.nthSuperUglyNumber(12, test))