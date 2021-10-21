"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
"""
从数组的最后一位开始找
如果是9 -> 该位变0, 9的数量+1,进入下一位
如果出现全是9的情况:9999 -> 10000则变成 [1] + [0] * (9的个数)
"""
class Solution:
    def plusOne(self, digits: list):
        num_of_nine = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                num_of_nine += 1
                digits[i] = 0
        return [1] + [0] * num_of_nine

s = Solution()
print(s.plusOne([9, 9, 9, 9]))  # -> [1, 0, 0, 0, 0]
print(s.plusOne([1, 9, 9, 9]))  # -> [2, 0, 0, 0]
print(s.plusOne([1, 2, 3, 4]))  # -> [1, 2, 3, 5]