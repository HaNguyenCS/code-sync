# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s = min(p.val, q.val)
        l = max(p.val, q.val)

        while root:
            if root.val > l:
                root = root.left
            elif root.val < s:
                root = root.right
            else:
                return root