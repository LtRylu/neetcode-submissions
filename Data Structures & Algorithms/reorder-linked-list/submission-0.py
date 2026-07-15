# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle, end = head, head
        while end.next and end.next.next:
            middle = middle.next
            end = end.next.next
        
        prev = None
        # need to reverse 2nd half of linked list
        if middle.next:
            cur = middle.next
            middle.next = None
        else: 
            cur = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        def zipper_merge(l1, l2):
            dummy = ListNode(0)
            tail = dummy

            while l1 and l2:
                next1 = l1.next
                next2 = l2.next

                tail.next = l1
                tail = tail.next

                tail.next = l2
                tail = tail.next

                l1 = next1
                l2 = next2

            if l1:
                tail.next = l1
            else:
                tail.next = l2

            return dummy.next
        zipper_merge(head, prev)


        
        
