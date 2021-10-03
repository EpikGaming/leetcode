import collections
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(node: TreeNode, cur: int):
            if not node:
                return 0
            res = 0
            cur += node.val
            res += prefix[cur - targetSum]
            prefix[cur] += 1
            print(res, cur)
            print(prefix)
            res += dfs(node.left, cur)
            res += dfs(node.right, cur)
            prefix[cur] -= 1
            return res
        return dfs(root, 0)

s = Solution()
a1 = TreeNode(10)
a2 = TreeNode(5)
a3 = TreeNode(-3)
a4 = TreeNode(3)
a5 = TreeNode(2)
a6 = TreeNode(11)
a7 = TreeNode(3)
a8 = TreeNode(-2)
a9 = TreeNode(1)
a1.left, a1.right = a2, a3
a2.left, a2.right = a4, a5
a3.right = a6
a4.left, a4.right = a7, a8
a5.right = a9
print(s.pathSum(a1, 8))