
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(a: 'Node'):
            if not a:
                return None
            if a in visited:
                return visited[a]
            copy = Node(a.val, [])
            visited[a] = copy
            for n in a.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)
