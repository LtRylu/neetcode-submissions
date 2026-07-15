# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we want the count of farthest depth of the left side of the tree 
            # vs the count of right side of the tree
        

        if not root:
            return True

        # Purpose is to count the depth of the inputted root node
        def depthCount(root, count): 
            if root.left and root.right: 
                return max(depthCount(root.left, count + 1), depthCount(root.right, count + 1)) 
            elif root.right: 
                return depthCount(root.right, count + 1) 
            elif root.left: 
                return depthCount(root.left, count + 1) 
            else: 
                return count



        left_count = 0
        right_count = 0
        count = 1
        if not self.isBalanced(root.right):
            return False
        if not self.isBalanced(root.left):
            return False
        
        if root.left:
            left_count = depthCount(root.left, count)
        if root.right:
            right_count = depthCount(root.right, count)
        if abs(left_count - right_count) <= 1:
            return True
        else: 
            return False
        
            