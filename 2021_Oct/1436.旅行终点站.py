"""
给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，
其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。
请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
"""
"""
由于终点站唯一，用Hash表存储所有的起始站cityAi
再遍历所有的cityBi找出唯一一个不存在于Hash表中的cityBi
"""
class Solution:
    def destCity(self, path: list):
        trace = {start: final for start, final in path}
        res = path[0][0]
        while trace[res] in trace:
            res = trace[res]

        return trace, res
        #trace: ->{'A': 'B', 'C': 'D', 'B': 'E', 'E': 'C', 'D': 'F'}
s = Solution()
test = [["A", "B"], ["C", "D"], ["B", "E"], ["E", "C"], ["D", "F"]]
print(s.destCity(test))     # ->D