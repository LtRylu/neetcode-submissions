# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathCount = 0

        def pathCounter(root, pathCount):

            if not root:
                return False

            pathCount += root.val

            if not root.left and not root.right:
                if pathCount == targetSum:
                    return True
                else:
                    return False
        
            if pathCounter(root.left, pathCount):
                return True
            if pathCounter(root.right, pathCount):
                return True
            pathCount -= root.val
            return False


        return pathCounter(root, pathCount)