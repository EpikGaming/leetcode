class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int):
        def function(a: int, b: int, tag=0):
            if a * b < 0:
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
                    res.append(")")
                    break
                res.append(str(n))
                dic[a] = i + 2
                if m == 0:
                    break
                i += 1
            return "-" + "".join(res) if flag == -1 else "".join(res)
        return function(numerator, denominator, 10000)

s = Solution()
test1 = [1, 5]
print(s.fractionToDecimal(test1[0], test1[1]))
