# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            ans = 1 if node.val >= max_val else 0

            max_val = max(max_val,node.val)
            ans += dfs(node.right, max_val)
            ans += dfs(node.left, max_val)

            return ans
        return dfs(root,float('-inf'))

