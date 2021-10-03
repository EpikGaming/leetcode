import heapq
class Solution:
    def kWeakestRows(self, mat: list, k: int):
        m, n = len(mat), len(mat[0])
        power = []
        res = []
        for i in range(m):
            l, r, pos = 0, n - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            power.append((pos + 1, i))

        heapq.heapify(power)
        for i in range(k):
            res.append(heapq.heappop(power)[1])
        return res

test = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
s = Solution()
print(s.kWeakestRows(test, 3))