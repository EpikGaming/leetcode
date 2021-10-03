import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list, capital: list):
        if w > max(capital):
            return sum(sorted(profits)[-k:])

        n = len(profits)
        cur = 0
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key=lambda x: x[0])
        hq = []
        for _ in range(k):
            while cur < n and arr[cur][0] <= w:
                heapq.heappush(hq, -arr[cur][1])
                cur += 1
            if hq:
                w -= heapq.heappop(hq)
            else:
                break
        return w


s = Solution()
profits = [1, 2, 3, 10, 3]
capital = [0, 1, 2, 6, 1]
print(s.findMaximizedCapital(3, 2, profits, capital))