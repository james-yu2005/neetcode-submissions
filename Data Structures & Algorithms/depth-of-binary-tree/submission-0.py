# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # in order, pre order, post order
        # left root right, root left right, left right root

        def postorder(node):
            if not node:
                return 0
            left = postorder(node.left)
            right = postorder(node.right)
            return 1 + max(left,right)
        return postorder(root)