"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        cloneMap = {}
        
        def duplicate(node):
            if node in cloneMap:
                return cloneMap[node]
            
            copy = Node(node.val)
            cloneMap[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(duplicate(n))

            return copy
        return duplicate(node) if node else None
        
        
        
        