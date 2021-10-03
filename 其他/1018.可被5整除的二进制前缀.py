class Solution:
    def prefixesDivBy5(self, A: list):
        result = []
        pre = 0
        for i in A:
            pre = ((pre << 1) + i) % 5
            result.append(not pre)
        return result


s = Solution()
test = [0, 1, 1, 1, 1, 1]
print(s.prefixesDivBy5(test))