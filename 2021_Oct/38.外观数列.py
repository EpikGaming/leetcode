"""
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
"""
"""
方法一.itertools
itertools模块对每一个新的字符串进行迭代操作
itertools.groupby()把迭代器中相邻的重复元素挑出来放在一起
方法二.模拟遍历
字符串操作，双指针判断长度
"""
import itertools
class Solution:
    def countArray(self, n: int):
        a, b = "1", "21"
        if n == 1:
            return a
        if n == 2:
            return b
        for _ in range(2, n):
            c = ""
            for key, group in itertools.groupby(b):
                c += str(len(list(group))) + str(key)
            a, b = b, c
        return b

    def countArray2(self, n: int):
        prev = "1"
        for _ in range(n - 1):
            cur = ""
            start, pos = 0, 0
            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos += 1
                cur += str(pos - start) + prev[start]
                start = pos
            prev = cur
        return prev


s = Solution()
print(s.countArray2(5))    # -> 111221