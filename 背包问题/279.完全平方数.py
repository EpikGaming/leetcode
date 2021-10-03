'''
给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）
使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；
换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
'''
class Solution:
    def numSquares(self, n: int):
        dp = [i for i in range(n + 1)]
        dp[0] = 0
        temp = int(n ** 0.5)
        nums = [i ** 2 for i in range(temp + 1)]
        print(nums)
        for i in range(1, n + 1):
            for j in nums:
                if i < j:
                    break
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp


s = Solution()
print(s.numSquares(13))
