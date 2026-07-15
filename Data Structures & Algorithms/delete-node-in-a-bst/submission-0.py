# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        # 2 cases:
            #Case 1 # Delete a node with 0 or 1 children
            #Case 2 # Delete a node with 2 children
                # We need the min or the right of the node
        
        # first we need to traverse the tree to the node to find the node / check its existence
        # we know if a node DNE if we reach the bottom of the tree

        if not root:
            return None
        if key > root.val:
            if root.right:
                root.right = self.deleteNode(root.right, key)
                return root
            else:
                return root
        elif key < root.val:
            if root.left: 
                root.left = self.deleteNode(root.left, key)
                return root
            else:
                return root
            return None

        # we are at the node to delete
        else:
            # case 1: 0 to 1 childs

            if root.right and not root.left:
                root = root.right
                return root
            elif root.left and not root.right:
                root = root.left
                return root
            elif not root.right and not root.left:
                root = None
                return root
            
            # case 2: 2 children

            elif root.right and root.left:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
                return root




