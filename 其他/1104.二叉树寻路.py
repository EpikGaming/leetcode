class Solution:
    def pathInZagTree(self, label: int):
        i = 0
        x = 1
        res = []
        while x <= label:
            x *= 2
            i += 1
        while i != 1:
            if i & 1:
                x //= 2
                res.append(label)
                temp = (label - x) // 2
                i -= 1
                label = x - 1 - temp
            else:
                res.append(label)
                temp = (x - 1 - label) // 2
                i -= 1
                x //= 2
                label = ((x // 2) + temp)
        res.append(1)
        return res[::-1]


s = Solution()
print(s.pathInZagTree(14))