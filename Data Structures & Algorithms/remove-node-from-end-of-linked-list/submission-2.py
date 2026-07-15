# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head

        while cur:
            cur = cur.next
            count += 1

        i = count - n - 1

        cur = head
        if i < 0:
            return head.next
        while i > 0:
            cur = cur.next
            i -= 1
        
        if cur.next:
            cur.next = cur.next.next
        else:
            return None

        return head
