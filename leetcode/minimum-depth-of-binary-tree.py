# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        minDepth = []
        q = deque([root])
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.right is None and cur.left is None:
                    return depth
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
            depth+=1
        return min(minDepth)