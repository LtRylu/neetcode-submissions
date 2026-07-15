"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}
        cur = head
        while cur:
            nodeMap[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                nodeMap[cur].next = nodeMap[cur.next]
            else:
                nodeMap[cur].next = None
            if cur.random:
                nodeMap[cur].random = nodeMap[cur.random]
            else:
                nodeMap[cur].random = None
            cur = cur.next
        if head: return nodeMap[head] 
        else: return None