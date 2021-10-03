import collections
class Solution:
    NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    def slidingPuzzle(self, board: list):
        def get(status: str):
            s = list(status)
            x = s.index("0")
            for y in Solution.NEIGHBORS[x]:
                s[x], s[y] = s[y], s[x]
                yield "".join(s)
                s[x], s[y] = s[y], s[x]

        initial = "".join(str(num) for num in sum(board, []))
        if initial == "123450":
            return 0
        q = collections.deque([(initial, 0)])
        visited = {initial}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in visited:
                    if next_status == "123450":
                        return step + 1
                    q.append((next_status, step + 1))
                    visited.add(next_status)
        return -1

test = [[4, 1, 2], [5, 0, 3]]
s = Solution()
print(s.slidingPuzzle(test))