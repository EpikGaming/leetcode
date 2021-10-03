class Solution:
    def combinationSum(self, candidates: list, target: int):
        candidates.sort()
        res = []
        path = []
        n = len(candidates)

        def dfs(x: int, path: list):
            if x == 0:
                res.append(path)