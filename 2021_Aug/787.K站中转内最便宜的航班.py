import collections
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flight: list, src: int, dst: int, k: int):
        if len(flight) == 0:
            return -1
        neighbours = collections.defaultdict(list)
        for i, j, p in flight:
            neighbours[i].append([j, p])
        visited = set()
        q = [src]
        while q:
            position = q.pop()
            visited.add(position)
            for nei, _ in neighbours[position]:
                if nei not in visited:
                    q.append(nei)

        if dst not in visited:
            return -1

        pq = [[0, -1, src]]
        while pq:
            price, passed, position = heapq.heappop(pq)
            if position == dst:
                return price
            for nei_position, nei_price in neighbours[position]:
                if passed + 1 <= k:
                    heapq.heappush(pq, [price + nei_price, passed + 1, nei_position])
        return -1


    def findCheapestPrice2(self, n: int, flight: list, src: int, dst: int, k: int):
        dp = [[float('inf')] * n for _ in range(k + 2)]
        dp[0][src] = 0
        for t in range(1, k + 2):
            for j, i, price in flight:
                dp[t][i] = min(dp[t][i], dp[t - 1][j] + price)

        res = min(dp[t][dst] for t in range(1, k + 2))
        return res, dp

    def findCheapestPrice3(self, n: int, flight: list, src: int, dst: int, k: int):
        dp = [float('inf')] * n
        dp[src] = 0
        res = float('inf')
        for t in range(1, k + 2):
            g = [float('inf')] * n
            for j, i, price in flight:
                g[i] = min(g[i], dp[j] + price)
            dp = g
            res = min(res, dp[dst])
            print(dp)
        return res

s = Solution()
test = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
print(s.findCheapestPrice3(3, test, 0, 2, 0))