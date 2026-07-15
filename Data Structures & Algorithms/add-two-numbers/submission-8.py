# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # the two lists can be different lengths thus we cannot just add the two from the beginning, we need to know the lengths

        long = l1
        short = l2
        flip = False
        while long and short:
            if short.next and not long.next:
                flip = True
                break
            long = long.next
            short = short.next
        if flip:
            long = l2
            short = l1
        else:
            long = l1
            short = l2
        
        cur = long
        while cur:
            if short:
                cur.val += short.val
                short = short.next
            if cur.val >= 10:
                if cur.next:
                    cur.next.val += cur.val // 10
                else:
                    cur.next = ListNode(cur.val // 10)
                cur.val = cur.val % 10
            cur = cur.next
        return long
            
        
