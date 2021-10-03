class Solution:
    def convertToTitle(self, columnNumber: int):
        res = []
        while columnNumber > 0:
            a0 = (columnNumber - 1) % 26 + 1
            res.append(chr(a0 - 1 + ord("A")))
            columnNumber = (columnNumber - a0) // 26
        return "".join(res[::-1])


    def convertToTitle2(self, columnNumber: int):
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            res.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26

        return "".join(res[::-1])

s = Solution()
test = 701
print(s.convertToTitle(test))
print(s.convertToTitle2(test))