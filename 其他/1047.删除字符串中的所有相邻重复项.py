class Solution:
    def removeDuplicates(self, S: str):
        n = len(S)
        stackA = []
        for i in range(n):
            if stackA and stackA[-1] == S[i]:
                stackA.pop()
            else:
                stackA.append(S[i])
        return "".join(stackA)

s = Solution()
test = "abbaca"
print(s.removeDuplicates(test))