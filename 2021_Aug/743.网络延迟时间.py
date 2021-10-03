class Solution:
    def networkDelayTime(self, times: list, n: int, k: int):
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x][y] = time
            g[y][x] = time
        print(g)
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
            used = [False] * n
            for _ in range(n):
                x = -1
                for y, u in enumerate(used):
                    if not u and (x == -1 or dist[i][y] < dist[i][x]):
                        x = y
                used[x] = True
                for y, time in enumerate(g[x]):
                    dist[i][y] = min(dist[i][y], dist[i][x] + time)
        return dist


s = Solution()
test = [[0, 1, 4], [0, 7, 8], [1, 2, 8], [1, 7, 11], [2, 3, 7], [2, 5, 4], [2, 8, 2], [3, 4, 9], [3, 5, 14], [4, 5, 10],
        [5, 6, 2], [6, 7, 1], [6, 8, 6], [7, 8, 7]]
print(s.networkDelayTime(test, 9, 1))
"""
Dijkstra最短路径
"""