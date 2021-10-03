class Solution:
    def flipAndInvertImage(self, A: list):
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range((n + 1) // 2):
                A[i][j], A[i][n - 1 - j] = 1 - A[i][n - 1 - j], 1 - A[i][j]
        return A

    def flipAndInvertImage2(self, A: list):
        return [[j ^ 1 for j in row[::-1]] for row in A]

test = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
test2 = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
s = Solution()
print(s.flipAndInvertImage(test))
print(s.flipAndInvertImage2(test2))

