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
"""
记录子树的节点树
left = 左子树个数
由于是二叉搜索树，左子树的节点值总是小于根节点值
如果left == k - 1,说明为根节点,直接返回node.val
如果left <  k - 1,说明目标节点在根节点的右子树,返回node.right
如果left >  k - 1,说明目标节点在根节点的左子树,返回node.left
"""
class MySolution:
    def __init__(self, root: TreeNode):
        self.root = root
        self._node_num = {}     # 表示每个节点，以它为根节点的树的节点数
        self._count_node_num(root)

    def kthSmallest2(self, k: int):
        node = self.root
        while node:
            left = self._get_node_num(node.left)
            if left == k - 1:
                return node.val
            elif left < k - 1:
                k -= left + 1
                node = node.right
            else:
                node = node.left

    def _count_node_num(self, node: TreeNode):
        if not node:
            return 0
        self._node_num[node] = 1 + self._count_node_num(node.left) + self._count_node_num(node.right)
        return self._node_num[node]

    def _get_node_num(self, node: TreeNode):
        return self._node_num[node] if node is not None else 0

    def test(self):
        print(self._node_num)
        #{a1: 5, a2: 3, a3: 1, a4: 1, a5:1}


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

    def kthSmallest2(self, root: TreeNode, k: int):
        bst = MySolution(root)
        bst.test()
        return bst.kthSmallest2(k)

a1 = TreeNode(5)
a2 = TreeNode(3)
a3 = TreeNode(6)
a4 = TreeNode(1)
a5 = TreeNode(4)
a1.left, a1. right = a2, a3
a2.left, a2.right = a4, a5
s = Solution()
print(s.kthSmallest2(a1, 4))
print(a1)
print(a2)