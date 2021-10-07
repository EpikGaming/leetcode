"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。
"""
"""
双指针：i遍历整个s，用j记录一个单词最后一个字符的索引值

优化思路：遇到非空格 -> 遇到了一个新单词,res += 1
遇到单词的判定：1. i == 0 and s[i] != " " ,即字符串开头无空格
             2. s[i - 1] == " " and s[i] != " " ,即前一个字符为空格，遇到了一个新单词
其余情况则跳过
1 + 2 -> (i == 0 or s[i - 1] == " ") and s[i] != " "
"""
class Solution:
    def countSegments(self, s: str):
        res = 0
        i, j = 0, 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                j = i
                while j < len(s) and s[j] != " ":
                    print(j)
                    j += 1
                res += 1
                i = j
                #print("i = " + str(i))
                #print(res)
        return res

    #优化
    def countSegments2(self, s: str):
        res = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == " ") and s[i] != " ":
                res += 1
        return res

s = Solution()
test = "   Hello,  my name is John"
print(s.countSegments2(test))   # -> 5