class Solution:
    def balanceStringSplit(self, s: str):
        res, d = 0, 0
        for ch in s:
            if ch == "L":
                d += 1
            else:
                d -= 1
            if d == 0:
                res += 1
        return res


s = Solution()
test = "LRLLRRLRLR"
print(s.balanceStringSplit(test))