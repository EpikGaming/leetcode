class UnionFind:
    def __init__(self, n):
        self.n = n
        self.father = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.rank[root_x] += self.rank[root_y]
        self.father[root_y] = root_x
        return True

class Solution:
    def minCostConnectPoints(self, points: list):
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        n = len(points)
        edges = list()
        uf = UnionFind(n)
        for i in range(n):
            for j in range(1, n + 1):
                edges.append((dist(i, j), i, j))
        edges.sort()
        result, num = 0, 1
        for length, x, y in edges:
            if uf.merge(x, y):
                result += length
                num += 1
                if num == n:
                    break
        return result

    def minCostConnectPoints_Kruskal(self, points: list):
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        edges = []
        n = len(points)
        for i in range(n - 1):
            for j in range(1, n):
                edges.append((dist(i, j), i, j))
        edges.sort()
        father = list(range(n))

        def find(x: int):
            if father[x] != x:
                father[x] = find(father[x])
            return father[x]
        result, num = 0, 0
        for length, x, y in edges:
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                father[root_y] = root_x
                num += 1
                result += length
            if num == n - 1:
                break
        return result