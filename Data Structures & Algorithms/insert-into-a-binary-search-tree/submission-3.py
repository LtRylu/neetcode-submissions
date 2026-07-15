# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        # Recursion Problem
        # Recursion needs a base case
            # -- Base case being that we reach. "leaf" node
            # not necessarily a leaf node but a node that can no longer go in the right direction of val
        if not root:
            root = TreeNode(val)
            return root
        if val > root.val:
            if root.right:
                root.right = self.insertIntoBST(root.right, val)
                return root
            else:
                root.right = TreeNode(val)
        elif val < root.val:
            if root.left:
                root.left = self.insertIntoBST(root.left, val)
                return root
            else:
                root.left = TreeNode(val)
        
        return root