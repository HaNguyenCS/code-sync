# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        maxDepth = 1

        q = deque([root])
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    maxDepth = max(maxDepth, depth)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
        return maxDepth