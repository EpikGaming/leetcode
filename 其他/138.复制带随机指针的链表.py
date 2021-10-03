import collections
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList_DFS(self, head: 'Node'):
        #1.从头结点开始
        #2.由于一个结点可能被多个结点指向，当一个结点被拷贝时，放入哈希表
        #3.先递归next，再递归random
        def dfs(node: 'Node'):
            if not node:
                return None
            if node in visited:
                return visited[node]
            copy = Node(node.val, None, None)
            visited[node] = copy
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)
            return copy
        visited = {}
        return dfs(head)

    def copyRandomList_BFS(self, head: 'Node'):
        #1.创建哈希表保存已拷贝的结点｛原结点： 拷贝结点｝
        #2.创建队列，并将头结点入队
        #3.当队列不为空时，弹出一个结点
        visited = {}

        def bfs(node: 'Node'):
            if not node:
                return node
            copy = Node(node.val, None, None)
            queue = collections.deque()
            queue.append(node)
            visited[node] = copy
            while queue:
                temp = queue.pop()
                if temp.next and temp.next not in visited:
                    visited[temp.next] = Node(temp.next.val, [], [])
                    queue.append(temp.next)
                if temp.random and temp.random not in visited:
                    visited[temp.random] = Node(temp.random.val, [], [])
                    queue.append(temp.random)
                visited[temp].next = visited.get(temp.next)
                visited[temp].random = visited.get(temp.random)
            return copy
        return bfs(head)