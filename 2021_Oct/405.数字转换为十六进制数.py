"""
给定一个整数，编写一个算法将这个数转换为十六进制数。
对于负整数，我们通常使用补码运算方法。
注意:
十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
"""
"""
位运算＋分组运算
将长度32位的进制转换成十六进制－>每4位1组，分8组转换
负数十六进制为原数二进制变反码后变补码
python中 -1 // 16 -> -1
"""
class Solution:
    def toHex(self, num: int):
        transList = "0123456789abcdef"
        #直接转换
        res = []
        for _ in range(8):
            res.append(num % 16)
            #此时res为结果倒序
            num //= 16
            print(num)
            if not num:
                break
                #当num为0时break
        print(res)
        return "".join(transList[n] for n in res[::-1])
s = Solution()
print(s.toHex(26))  # res -> [10, 1] -> 1a
print(s.toHex(-1))  # res -> [15, 15, 15, 15, 15, 15, 15, 15] -> ffffffff
print(s.toHex(-5))  # res -> [11, 15, 15, 15, 15, 15, 15, 15] -> fffffffb