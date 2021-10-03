class Solution:
    def compareVersion(self, version1: str, version2: str):
        A = list(map(int, version1.split(".")))
        B = list(map(int, version2.split(".")))
        m, n = len(A), len(B)
        if m > n:
            B = B + [0] * (m - n)
        else:
            A = A + [0] * (n - m)
        i, j = 0, 0
        if A == B:
            return 0
        while i < m or j < n:
            if A[i] == B[j]:
                i += 1
                j += 1
            elif A[i] < B[j]:
                return -1
            else:
                return 1
        return 0

    def compareVersion2(self, version1: str, version2: str):
        m, n = len(version1), len(version2)
        i, j = 0, 0
        while i < m or j < n:
            x = 0
            while i < m and version1[i] != ".":
                x = x * 10 + ord(version1[i]) - ord("0")
                i += 1
            i += 1

            y = 0
            while j < n and version2[j] != ".":
                y = y * 10 + ord(version2[j]) - ord("0")
                j += 1
            j += 1
            if x != y:
                return 1 if x > y else -1
        return 0


s = Solution()
print(s.compareVersion2("7.5.2.4", "7.5.3"))