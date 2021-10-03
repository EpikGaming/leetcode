class Solution:
    def checkRecord(self, s: str):
        i, j = 0, 0
        for c in s:
            if c == "P":
                j = 0
                continue
            elif c == "A":
                i += 1
                j = 0
                if i == 2:
                    return False
            else:
                j += 1
                if j == 3:
                    return False
        return True

s = Solution()
print(s.checkRecord("PPALLPL"))