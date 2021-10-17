"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，
请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
"""
"""
树的中序遍历
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        res = []

        def dfs(node: TreeNode):
            if not node:
                return
            if node.left:
                dfs(node.left)
            res.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return res

a1 = TreeNode(3)
a2 = TreeNode(1)
a3 = TreeNode(4)
a4 = TreeNode(2)
a1.left, a1. right = a2, a3
a2.right = a4
s = Solution()
print(s.kthSmallest(a1, 2))