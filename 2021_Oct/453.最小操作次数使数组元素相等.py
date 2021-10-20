"""
给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。
返回让数组所有元素相等的最小操作次数。
"""
"""
使n - 1个元素增加1的操作等同于让1个元素减1，两者所用的步数是一致的
"""
class Solution:
    def minMoves(self, nums: list):
        temp = min(nums)
        res = 0
        for num in nums:
            res += num - temp
        return res

s = Solution()
test = [2, 3, 4]
print(s.minMoves(test))