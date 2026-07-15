# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        mainList = [[root]]
        mainListV = [[root.val]]
        i = 0
        while i < len(mainList):
            subList = []
            subListV = []
            j = 0
            while j < len(mainList[i]):
                if mainList[i][j].left:
                    subList.append(mainList[i][j].left)
                    subListV.append(mainList[i][j].left.val)
                if mainList[i][j].right:
                    subList.append(mainList[i][j].right)
                    subListV.append(mainList[i][j].right.val)
                j += 1
            i += 1
            if len(subList) > 0:
                mainList.append(subList)
                mainListV.append(subListV)
        return mainListV