"""
给定两个整数，分别表示分数的分子numerator 和分母denominator，
以字符串形式返回小数。
如果小数部分为循环小数，则将循环的部分括在括号内。
如果存在多个答案，只需返回任意一个。
对于所有给定的输入，保证答案字符串的长度小于 10^4 。
"""
"""
模拟除法，对余数乘10
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int):
        def function(a: int, b: int, tag=0):
            #把符号去掉，方便处理
            if a * b < 0:
                #由于python无数据类型溢出，所以可以直接相乘
                flag = -1
            else:
                flag = 1
            a, b = abs(a), abs(b)
            m = a % b
            n = a // b
            if not m:
                return str(n * flag)
            res = [str(n), '.']
            dic = {}
            i = 0
            while i < tag:
                a = m * 10
                m = a % b
                n = a // b
                if a in dic:
                    res.insert(dic[a], "(")
                    #列表循环部分前插入"("
                    res.append(")")
                    break
                res.append(str(n))
                dic[a] = i + 2
                #前两位是整数部分str(n)和小数点"."所以字典值为i+2,起始值为0+2=2
                if m == 0:
                    break
                i += 1
            return "-" + "".join(res) if flag == -1 else "".join(res)
        return function(numerator, denominator, 10000)
        #由于答案字符串长度小于10^4,所以tag=10000

s = Solution()
print(s.fractionToDecimal(1, 5))  # ->0.2
print(s.fractionToDecimal(4, 333))  # ->0.(012)
