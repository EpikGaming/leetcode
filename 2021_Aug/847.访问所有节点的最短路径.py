import collections
class Solution:
    def shortestPathLength(self, graph: list):
        n = len(graph)
        q = collections.deque((i, 1 << i, 0) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)}
        ans = 0
        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                ans = dist
                break
            for v in graph[u]:
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist + 1))
                    seen.add((v, mask_v))
        return ans, seen

s = Solution()
test = [[1, 2, 3], [0], [0], [0]]
print(s.shortestPathLength(test))