"""
你总共有n枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，
其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
给你一个数字n ，计算并返回可形成 完整阶梯行 的总行数。
"""
"""
累加while判断，最后结果为i - 1,所以是while sums <= n
优化：二分法，等差数列前n项合 Sn = k * (k + 1) / 2
查找计算n枚硬币可以形成的总行数
"""
class Solution:
    def arrangeCoins(self, n: int):
        sums = 0
        i = 0
        while sums <= n:
            i += 1
            sums += i
        return i - 1

    def arrangeCoins2(self, n: int):
        left, right = 1, n
        while left < right:
            #使mid更靠右
            mid = (left + right + 1) // 2
            #mid太小
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left

s = Solution()
print(s.arrangeCoins2(1))   # -> 1
print(s.arrangeCoins2(15))  # -> 5