# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # the two lists can be different lengths thus we cannot just add the two from the beginning, we need to know the lengths
        c1 = 0
        cur = l1
        while cur:
            cur = cur.next
            c1 += 1
        c2 = 0
        cur = l2
        while cur:
            cur = cur.next
            c2 += 1
        
        if c1 >= c2:
            long = l1
            longC = c1
            short = l2
            shortC = c2
        else:
            long = l2
            longC = c2
            short = l1
            shortC = c2
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
            
        
