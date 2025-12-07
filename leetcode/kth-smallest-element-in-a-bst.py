# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        s = []
        arr = []

        while root or s:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                arr.append(root.val)
                root = root.right
            
        return arr[k-1]