"""
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
"""
"""
模拟，用a，b，c三个数分别存放第一第二第三大的数
"""
class Solution:
    def thirdMax(self, nums: list):
        a, b, c = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif a > num > b:
                a, b, c = a, num, b
            elif b > num > c:
                a, b, c = a, b, num
                #当c仍为无穷小时说明c不存在，则返回最大的数
        return c if c != float('-inf') else a


s = Solution()
test1 = [1,1,1,1,1,2,2,2,2,2]
print(s.thirdMax(test1))    # -> 2
test2 = [1,2,3]
print(s.thirdMax(test2))    # -> 1