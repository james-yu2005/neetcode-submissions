# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # in order, pre order, post order
        # left root right, root left right, left right root
        # probably post order is most useful
        length = 0
        def postorder(root):
            nonlocal length
            if not root:
                return 0
            left = postorder(root.left)
            right = postorder(root.right)
            length = max(length,right+left)
            return 1 + max(right,left)
        postorder(root)
        return length
        