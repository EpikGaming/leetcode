"""
有一个密钥字符串S，只包含字母，数字以及 '-'（破折号）。
其中，N个'-'将字符串分成了N+1组。
给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。
特别地，第一个分组包含的字符个数必须小于等于 K，
但至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，
并且将所有的小写字母转换为大写字母。
给定非空字符串S和数字K按照上面描述的规则进行格式化。
"""
"""
模拟，从后往前遍历，遇到k个数字或字母后添加"-"
当字符串正好被分成n个组时，会多出来一个"-"需要判断res[-1] == "-"
特殊处理：当字符串S只有"-"时 res = []，需要判断 if res
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int):
        res = []
        temp = 0
        for i in range(len(s) - 1, -1, -1):
            #从后往前遍历
            if s[i] != "-":
                res.append(s[i].upper())
                #小写字母变大写
                temp += 1
                if temp % k == 0:
                    res.append("-")
        if res and res[-1] == "-":
            #特殊情况处理
            res.pop()
        return "".join(res[::-1])
        #此时为答案倒序，需要处理res
s = Solution()
test = "5F3Z-2E9W"
print(s.licenseKeyFormatting(test, 4))  # -> 5F3Z-2E9W
print(s.licenseKeyFormatting(test, 3))  # -> 5F-3Z2-E9W