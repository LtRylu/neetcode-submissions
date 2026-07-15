# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            if (not p or not q) or p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        cur = False
        if root.val == subRoot.val:
            cur = isSameTree(root, subRoot)
        
        return left or right or cur