class Solution:
    def escapeGhost(self, ghosts: list, target: list):
        source = [0, 0]

        def manhattanDistance(A: list, B: list):
            return abs(A[0] - B[0]) + abs(A[1] - B[1])

        distance = manhattanDistance(source, target)
        return all(manhattanDistance(ghost, target) > distance for ghost in ghosts)

s = Solution()
testA = [[1, 0]]
print(s.escapeGhost(testA, [2, 0]))