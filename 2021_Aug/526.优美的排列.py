import collections
class Solution:
    def countArrangement(self, n: int):
        match = collections.defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)

        num = 0
        visited = set()

        def traceback(x: int):
            if x == n + 1:
                nonlocal num
                num += 1
                return

            for i in match[x]:
                if i not in visited:
                    visited.add(i)
                    traceback(x + 1)
                    visited.remove(i)

        traceback(1)
        return num


s = Solution()
print(s.countArrangement(3))