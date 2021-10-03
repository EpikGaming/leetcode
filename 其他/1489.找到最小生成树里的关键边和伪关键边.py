class UnionFind:
    def __init__(self, n: int):
        self.father = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n

    def find(self, x: int):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_y] > self.size[root_x]:
            root_x, root_y = root_y, root_x
        self.father[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.setCount -= 1
        return True

    def isConnect(self, x, y):
        return self.father[x] == self.father[y]


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list):
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        uf_std = UnionFind(n)
        value = 0
        for i in range(m):
            if uf_std.merge(edges[i][0], edges[i][1]):
                value += edges[i][2]
        print(value)
        result = [list(), list()]

        for i in range(m):
            #找关键边
            uf = UnionFind(n)
            v = 0
            for j in range(m):
                if i != j and uf.merge(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if uf.setCount != 1 or (uf.setCount == 1 and v > value):
                result[0].append(edges[i][3])
                continue

            #找伪关键边
            uf = UnionFind(n)
            uf.merge(edges[i][0], edges[i][1])
            v = edges[i][2]
            print(uf.size)
            for j in range(m):
                if i != j and uf.merge(edges[j][0], edges[j][1]):
                    v += edges[j][2]
                    print(v)
                    print(i, j)
                    print(uf.father)
            if v == value:
                result[1].append(edges[i][3])
        return result

s = Solution()
test = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
print(s.findCriticalAndPseudoCriticalEdges(5, test))