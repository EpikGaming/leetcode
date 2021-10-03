class Solution:
    def permutation(self, s: str):
        res = []
        n = len(s)
        c = list(s)

        def dfs(x):
            if x == n - 1:
                res.append("".join(c))
                return

            dic = set()
            for i in range(x, n):
                if c[i] in dic:
                    continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res

test = "abc"
s = Solution()
print(s.permutation(test))
