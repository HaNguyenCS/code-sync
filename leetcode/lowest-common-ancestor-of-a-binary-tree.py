# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        queue = deque([root])
        parents = {root: None}

        while queue:
            cur = queue.popleft()

            if cur.left:
                queue.append(cur.left)
                parents[cur.left] = cur
            
            if cur.right:
                queue.append(cur.right)
                parents[cur.right] = cur
            
            if p in parents and q in parents:
                break
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        while q:
            if q in ancestors:
                return q
            q = parents[q]