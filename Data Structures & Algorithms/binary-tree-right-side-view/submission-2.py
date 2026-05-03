# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = [root.val]
        level = 1

        while q:
            level += 1
            for i in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                    if len(ans) < level:
                        ans.append(node.right.val)
                if node.left:
                    q.append(node.left)
                    if len(ans) < level:
                        ans.append(node.left.val)
        return ans


