# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sort = []
        q = []
        while root or q:
            if root:
                q.append(root)
                root = root.left
            else:
                root = q.pop()
                sort.append(root.val)
                root = root.right

        n = len(sort)
        mid = floor(n/2)
        root = TreeNode(sort[mid])

        queue = deque()
        
        queue.append((root, 0, mid-1))
        queue.append((root, mid+1, n-1))

        while queue:
            parent, left, right = queue.popleft()
            if left <= right:
                mid = (left+right)//2
                child = TreeNode(sort[mid])

                if sort[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child
                queue.append((child, left, mid-1))
                queue.append((child, mid+1, right))
        return root