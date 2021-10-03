class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        res = []
        parent = dict()

        def findParents(node: TreeNode):
            if node.left:
                parent[node.left.val] = node
                findParents(node.left)
            if node.right:
                parent[node.right.val] = node
                findParents(node.right)

        def findRes(node: TreeNode, fromNode: TreeNode, depth: int):
            if not node:
                return
            if depth == k:
                res.append(node.val)
                return
            if node.left != fromNode:
                findRes(node.left, node, depth + 1)
            if node.right != fromNode:
                findRes(node.right, node, depth + 1)
            if node in parent and parent[node] != fromNode:
                findRes(parent[node], node, depth + 1)

        findParents(root)
        findRes(target, None, 0)
        return res
