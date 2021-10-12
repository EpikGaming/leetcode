"""
给定两个整数，被除数dividend和除数divisor。将两数相除，
要求不使用乘法、除法和 mod 运算符。
返回被除数dividend除以除数divisor得到的商。
整数除法的结果应当截去（truncate）其小数部分，
例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
"""
"""
位运算依次判断，当只能存储32位有效数字的时候，记得判断最大值和最小值情况
"""
class Solution:
    def divide(self, dividend: int, divisor: int):
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        if dividend == 0:
            return 0
        res = 0
        i = 0
        if dividend * divisor < 0:
            flag = -1
        else:
            flag = 1
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend - (divisor << i) >= 0:
            dividend -= (divisor << i)
            res += 1 if i == 0 else 1 << i
            i += 1
        for j in range(i, -1, -1):
            if dividend >= divisor << j:
                dividend -= divisor << j
                res += 1 if j == 0 else 1 << j
            else:
                continue
        return res * flag


s = Solution()
print(s.divide(3, 3))