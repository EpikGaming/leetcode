class Solution:
    def destCity(self, path: list):
        trace = {start: final for start, final in path}
        res = path[0][0]
        while trace[res] in trace:
            res = trace[res]

        return trace, res
s = Solution()
test = [["A", "B"], ["C", "D"], ["B", "E"], ["E", "C"], ["D", "F"]]
print(s.destCity(test))