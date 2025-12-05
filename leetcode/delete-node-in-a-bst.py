# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        cur = root
        prev = None

        while cur and cur.val != key:
            prev = cur
            if key < cur.val:
                cur = cur.left
            elif key > cur.val:
                cur = cur.right

        if not cur:
            return root
        if not cur.left and not cur.right:
            if not prev:
                return None
            if prev.left == cur:
                prev.left = None
            else:
                prev.right = None
        
        elif not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not prev:
                return child
            if prev.left == cur:
                prev.left = child
            else:
                prev.right = child
        
        else:
            parent = cur
            suc = cur.right

            while suc.left:
                parent = suc
                suc = suc.left
            
            cur.val = suc.val

            if parent.left == suc:
                parent.left = suc.right #delete the left side bc we alr copied the value to cur
            else:
                parent.right = suc.right
        return root