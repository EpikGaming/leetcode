class Solution:
    def reverseStr(self, s: str, k: int):
        def reverse(A: list, left: int, right: int):
            while left < right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        t = list(s)
        n = len(t)
        for i in range(0, n, 2 * k):
            reverse(t, i, i + k - 1) if i + k - 1 < n else reverse(t, i, n - 1)
        return t


s = Solution()
test = "abcdefg"
print(s.reverseStr(test, 3))