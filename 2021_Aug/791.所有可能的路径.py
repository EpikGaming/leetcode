class Solution:
    def allPathSourceTarget(self, graph: list):
        res = []
        temp = []

        def dfs(x: int):
            if x == len(graph) - 1:
                res.append(temp[:])

            for y in graph[x]:
                temp.append(y)
                dfs(y)
                temp.pop()

        temp.append(0)
        dfs(0)
        return res

s = Solution()
test = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print(s.allPathSourceTarget(test))