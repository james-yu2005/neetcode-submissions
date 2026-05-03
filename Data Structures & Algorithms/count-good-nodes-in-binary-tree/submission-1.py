# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = []

        def dfs(node, max_val):
            if not node:
                return 
            if node.val >= max_val:
                good.append(0)
            max_val = max(max_val,node.val)
            dfs(node.right, max_val)
            dfs(node.left, max_val)
        dfs(root,float('-inf'))
        return len(good)

