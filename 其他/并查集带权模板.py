class UnionFind:
    def __init__(self):
        """
        记录每个节点的父节点
        记录每个节点到根节点的权重
        """
        self.father = {}
        self.value = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        更新权重
        """
        root = x
        base = 1
        #节点更新权重的时候需要放大的倍数
        while self.father[root] != None:
            root = self.father[root]
            base *= self.value[root]
        while x != root:
            original_father = self.father[x]
            self.value *= base
            base /= self.value[original_father]
            self.father[x] = root
            x = original_father
        return root

    def merge(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.value[root_x] = self.value[root_y] * val / self.value[x]

    def is_connection(self, x, y):
        return x in self.value and y in self.value and self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.father:
            self.father = None
            self.value[x] = 1.0


class Solution:
    def calcEquation(self, equations: list, values: list, queries: list):
        uf = UnionFind()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)

        result = [-1.0] * len(queries)
        for i, (a, b) in enumerate(queries):
            if uf.is_connection(a, b):
                result[i] = uf.value[a] / uf.value[b]
        return result