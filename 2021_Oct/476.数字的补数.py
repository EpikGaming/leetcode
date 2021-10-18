"""
对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。

例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
给你一个整数 num ，输出它的补数。
"""

class Solution:
    def function(self, n: int):
        temp = bin(n)
        print("test", temp)
        res = 0
        j = 1
        for i in range(len(temp) - 1, 0, -1):
            res += j if temp[i] == "0" else 0
            j *= 2
        return res


s = Solution()
print(s.function(5))
print(s.function(10))