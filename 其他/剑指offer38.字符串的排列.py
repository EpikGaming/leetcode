class Solution:
    def permutation(self, s: str):
        c = list(s)
        res = []

        def dfs(n):
            if n == len(s) - 1:
                res.append("".join(c))
                return

            dic = set()
            for i in range(n, len(s)):
                if c[i] in dic:
                    continue
                dic.add(c[i])
                c[i], c[n] = c[n], c[i]
                dfs(n + 1)
                c[i], c[n] = c[n], c[i]
        dfs(0)
        return res


test = 'abbc'
s = Solution()
print(s.permutation(test))