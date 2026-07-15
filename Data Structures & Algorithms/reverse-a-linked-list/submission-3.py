# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        old = None
        cur = head
        new = None
        if head is None:
            return None
        
        while cur.next != None:
            new = cur.next

            cur.next = old
            old = cur
            cur = new
        
        cur.next = old

        return cur
            


