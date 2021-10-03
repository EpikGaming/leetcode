class Solution:
    def eventualSafeNodes(self, graph: list):
        n = len(graph)
        color = [0] * n

        def safe(x: int):
            if color[x] > 0:
                return color[x] == 2
            color[x] = 1
            for y in graph[x]:
                if not safe(y):
                    return False
            color[x] = 2
            return True

        #return [i for i in range(n) if safe(i)]
        for i in range(n):
            safe(i)
        return color

s = Solution()
test = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(s.eventualSafeNodes(test))
"""
1.深搜＋三色标记
白色0——初始节点，灰色1——进入递归栈的节点，黑色2——安全的节点
2.对于每个初始节点，总是搜索它的目标节点
如果递归栈中存在灰色节点，那么：
    该递归栈中的节点形成环，都是不安全的节点
3.否则，则是安全的节点，返回所有颜色为2的节点
"""