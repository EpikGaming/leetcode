import heapq
class Solution:
    def nthUglyNumber(self, n: int):
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            cur = heapq.heappop(heap)
            for factor in factors:
                if cur * factor not in seen:
                    temp = cur * factor
                    heapq.heappush(heap, temp)
                    seen.add(temp)
        return heapq.heappop(heap)

    def nthUglyNumbers(self, n: int):
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp

s = Solution()
print(s.nthUglyNumber(1))
print(s.nthUglyNumbers(12))