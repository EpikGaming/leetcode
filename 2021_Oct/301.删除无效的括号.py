class Solution:
    def removeInvalidParentheses(self, s: str):
        res = []
        lremove, rremove = 0, 0
        for c in s:
            if c == "(":
                lremove += 1
            elif c == ")":
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def isValid(string):
            cnt = 0
            for c in string:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lre, rre):
            if lre == 0 and rre == 0:
                if isValid(s):
                    res.append(s)
                return

            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                if lre + rre > len(s) - 1:
                    break
                if lre > 0 and s[i] == "(":
                    helper(s[:i] + s[i + 1:], i, lre - 1, rre)
                if rre > 0 and s[i] == ")":
                    helper(s[:i] + s[i + 1:], i, lre, rre - 1)
        helper(s, 0, lremove, rremove)
        return res

s = Solution()
test = "(a)())()"
print(s.removeInvalidParentheses(test))