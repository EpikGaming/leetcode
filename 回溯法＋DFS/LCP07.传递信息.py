import collections
class Solution:
    def numWays(self, n: int, relation: list, k: int):
        self.ways = 0
        self.n = n
        self.k = k
        self.edgs = collections.defaultdict(list)

        for start, end in relation:
            self.edgs[start].append(end)

        self.dfs(0, 0)
        return self.ways

    def dfs(self, index, step):
        if step == self.k:
            if index == self.n-1:
                self.ways += 1
            return

        for to in self.edgs[index]:
            self.dfs(to, step + 1)


n = 5
relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
k = 3
s = Solution()
print(s.numWays(n, relation, k))


