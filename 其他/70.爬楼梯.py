class Solution:
    def climbStairs(self, n: int):
        p, q, res = 0, 0, 1
        for i in range(1, n + 1):
            p = q
            q = res
            res = p + q
        return res

    def matrixMult(self, matrixA: list, matrixB: list):
        matrixC = [[sum(a * b for a, b in zip(m1, m2)) for m2 in zip(*matrixB)] for m1 in matrixA]
        return matrixC

    def climbStairs2(self, n : int):
        if n == 1:
            return 1
        A = [[1, 1], [1, 0]]
        res = [[1, 0], [0, 1]]
        while n:
            if n & 1:
                res = self.matrixMult(res, A)
            A = self.matrixMult(A, A)
            n >>= 1
            print(A)
        return res[0][0]

s = Solution()
print(s.climbStairs(4))
print(s.climbStairs2(4))