class Solution:
    def fib(self, n: int):
        MOD = 1000000007

        def matrixMult(matrixA: list, matrixB: list):
            return [[sum(a * b for a, b in zip(m1, m2)) % MOD for m2 in zip(*matrixB)]for m1 in matrixA]

        if n == 1:
            return 1
        A = [[1, 1], [1, 0]]
        temp = [[1, 0], [0, 1]]
        while n:
            if n & 1:
                res = matrixMult(A, temp)
            A = matrixMult(A, A)
            n >>= 1

        return res

s = Solution()
print(s.fib(5))