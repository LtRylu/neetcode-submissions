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

        def dfs(root, interval):
            # Define base case: (We reach a leaf node, we know it is a valid subtree)
            if not root:
                return True
            

            if root.val <= interval[0] or root.val >= interval[1]:
                return False
            left_valid = True
            right_valid = True
            if root.left:
                left_valid = dfs(root.left, [interval[0], root.val])
            if root.right:
                right_valid =  dfs(root.right, [root.val, interval[1]])
            
            return left_valid and right_valid

        return dfs(root, [float('-inf'), float('inf')])

