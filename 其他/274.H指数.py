class Solution:
    def hIndex(self, citation: list):
        n = len(citation)
        tot = 0
        counter = [0] * (n + 1)
        for c in citation:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        print(counter)
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0

s = Solution()
test = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 100]
print(s.hIndex(test))