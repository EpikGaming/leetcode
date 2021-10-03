import collections
class Solution:
    def numWays(self, n: int, relation: list, k: int):
        edges = collections.defaultdict(list)
        for edge in relation:
            start = edge[0]
            end = edge[1]
            edges[start].append(end)

        q = collections.deque([0])
        step = 0
        while q and step < k:
            step += 1
            for i in range(len(q)):
                status = q.popleft()
                to = edges[status]
                for next_status in to:
                    q.append(next_status)
        res = 0
        if step == k:
            while q:
                if q.popleft() == n - 1:
                    res += 1
        return res