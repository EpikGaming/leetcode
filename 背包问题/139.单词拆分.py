class Solution:
    def wordBreak(self, s: str, wordDict: list):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i: j] in wordDict:
                    dp[j] = True
        return dp

s = Solution()
test = "leetcode"
listA = ['leet', 'be', 'co', 'de']
print(s.wordBreak(test, listA))