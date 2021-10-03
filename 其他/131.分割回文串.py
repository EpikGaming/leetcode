class Solution:
    def partition(self, s: str):
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]
        print(f)

        ret = []
        ans = []
        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                print("i = %d" %i)
                print("ret")
                print(ret)
                return

            for j in range(i, n):
                if f[i][j]:
                    print("f[%d][%d]" %(i, j))
                    ans.append(s[i: j + 1])
                    print("ans1")
                    print(ans)
                    print(j)
                    dfs(j + 1)
                    ans.pop()
                    print("ans2")
                    print(ans)
        dfs(0)
        return ret

s = Solution()
test = "aab"
print(s.partition(test))