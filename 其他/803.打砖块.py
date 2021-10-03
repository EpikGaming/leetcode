class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}

    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]

    def find(self, x):
        if not self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.size_of_set[root_y] += self.size_of_set[root_x]
            del self.size_of_set[root_x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.size_of_set[x] = 1

class Solution:
    def __init__(self):
        self.CEILING = (-1, -1)
        self.DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def is_valid(self, x, y, grid, m, n):
        return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

    def hitBricks(self, grid: list, hits: list):
        uf = UnionFind()
        m, n = len(grid), len(grid[0])
        res = [0] * len(hits)
        #初始化
        uf.add(self.CEILING)
        #敲掉
        for x, y in hits:
            grid[x][y] -= 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uf.add((i, j))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    #合并剩余砖块
                    for dx, dy in self.DIRECTION:
                        nx, ny = i + dx, j + dy
                        if not self.is_valid(nx, ny, grid, m, n):
                            continue
                        uf.merge((i, j), (nx, ny))

        for j in range(n):
            if grid[0][j] == 1:
                uf.merge((0, j), self.CEILING)

        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]
            #还原
            grid[x][y] += 1
            #错误输入判定
            if grid[x][y] != 1:
                continue
            #敲完后与天花板连接的数量
            after_hit = uf.get_size_of_set(self.CEILING)
            #填充，合并
            uf.add((x, y))
            for dx, dy in self.DIRECTION:
                nx, ny = x + dx, y + dy
                if not self.is_valid(nx, ny, grid, m, n):
                    continue
                uf.merge((x, y), (nx, ny))
            if x == 0:
                uf.merge((x, y), self.CEILING)

            if uf.is_connected((x, y), self.CEILING):
                before_hit = uf.get_size_of_set(self.CEILING)
                res[i] = before_hit - after_hit - 1
        return res