# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def post(p,q):
            if not p and not q:
                return True
            if p and not q:
                return False
            if not p and q:
                return False
            
            if q.val != p.val:
                return False
            
            return post(q.right, p.right) and post(q.left,p.left)
        return post(p,q)