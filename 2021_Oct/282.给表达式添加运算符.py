"""
给定一个仅包含数字0-9的字符串 num 和一个目标值整数 target ，
在 num 的数字之间添加 二元 运算符（不是一元）+、-或*，返回所有能够得到目标值的表达式。
"""
"""
回溯法
定义 traceback(expr, i, temp, mul)
expr：记录当前表达式
i：记录当前num指向的数字，当i == len(num)时查看结果temp与target的关系
temp：当前表达式expr所形成的结果
mul：当前表达式最后一个连乘的结果，以备出现乘号时使用
例子：
num = 1234
expr = ['1', '-', '2']，此时temp = -1, mul = -2
当j = 3, val = num[j] = 3
对于加号+：expr = 1-2+3,temp = -1 + 3 = 2, mul = 3
         temp = temp + val, mul = val
         
对于减号-：expr = 1-2-3,temp = -1 - 3 = -4,mul = -3
         temp = temp - val, mul = -val
         
对于乘号*：expr = 1-2*3,上一步的temp不再是-1，而是1(-1 - (-2)),即(temp - mul)
         temp = (-1 - (-2)) + (-2 * 3),mul = -6
         temp = (temp - mul + mul * val), mul = mul * val
"""
class Solution:
    def addOperators(self, num: str, target: int):
        n = len(num)
        res = []

        def traceback(expr: list, i: int, temp: int, mul: int):
            #print(expr, i, temp, mul)
            #i == n,判断结果，如果temp == target,表达式放入结果集
            if i == n:
                if temp == target:
                    res.append("".join(expr))
                return
            #符号位为expr最后一位
            signIndex = len(expr)
            #i == 0时只能为数字，不能为符号
            if i > 0:
                #为signIndex创造一个空间 signIndex = len(expr)，但是expr最后一个索引是len(expr) - 1
                expr.append("")
            val = 0
            for j in range(i, n):       # 枚举截取数字长度 1+2,1+23,1+234
                if j > i and num[i] == "0":     # 数字可以是单个0，但不能有前导0
                    break
                val = val * 10 + int(num[j])    # 2,23,234
                expr.append(num[j])
                if i == 0:
                    #如果i == 0 表示表达式开头，表达式开头不能为符号
                    #traceback(1, 1, 1, 1),traceback(12, 2, 12, 12), traceback(123, 3, 123, 123)...
                    traceback(expr, j + 1, val, val)
                else:
                    expr[signIndex] = "+"
                    traceback(expr, j + 1, temp + val, val)
                    expr[signIndex] = "-"
                    traceback(expr, j + 1, temp - val, -val)
                    expr[signIndex] = "*"
                    traceback(expr, j + 1, temp - mul + mul * val, mul * val)
            #回溯法恢复现场
            #1+2+3不符合，则把表达式恢复成1+2与之后的3重新做回溯,变成回溯检测1+2-3,1+2*3
            del expr[signIndex:]

        traceback([], 0, 0, 0)
        return res

s = Solution()
print(s.addOperators("105", 5))

