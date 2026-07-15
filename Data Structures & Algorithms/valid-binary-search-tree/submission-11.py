# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # when going left, it has to be less than everything prior to it
        # when going right, it has to be greater than everything prior to it

        def dfs(root, left, right):
            # Define base case: (We reach a leaf node, we know it is a valid subtree)
            if not root:
                return True
        
            if not (root.val > left and root.val < right):
                return False
            
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
            

        return dfs(root, float('-inf'), float('inf'))

