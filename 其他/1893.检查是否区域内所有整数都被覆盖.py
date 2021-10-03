class Solution:
    def isCovered(self, ranges: list, left: int, right: int):
        res = [False] * (right - left + 1)
        for i in range(right - left + 1):
            for begin, end in ranges:
                if res[i]:
                    continue
                if begin <= left + i <= end:
                    res[i] = True
        return res.count(True) == len(res)

s = Solution()
test = [[25,42],[7,14],[2,32],[25,28],[39,49],[1,50],[29,45],[18,47]]
print(s.isCovered(test, 15, 38))