import collections
class Solution:
    def snakesAndLadders(self, board: list):
        n = len(board)

        def id2rc(idx: int):
            r = (idx - 1) // n
            c = (idx - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        visited = set()
        q = collections.deque([(1, 0)])
        while q:
            idx, step = q.popleft()
            for i in range(1, 6 + 1):
                idx_next = idx + i
                if idx_next > n * n:
                    break

                x_next, y_next = id2rc(idx_next)
                if board[x_next][y_next] > 0:
                    idx_next = board[x_next][y_next]
                if idx_next == n * n:
                    return step + 1
                if idx_next not in visited:
                    q.append((idx_next, step + 1))
                    visited.add(idx_next)
        return -1