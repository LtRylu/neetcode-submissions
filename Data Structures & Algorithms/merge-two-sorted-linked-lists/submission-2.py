# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not list1 or not list2:
            if list1:
                return list1
            if list2:
                return list2
            else:
                return None

        if list1.val <= list2.val:
            cur = list1
            other = list2
        else:
            cur = list2
            other = list1
        
        startHead = cur
        
        while cur.next:
            if other.val < cur.next.val:
                tmp = cur.next
                cur.next = other
                other = tmp
            else:
                cur = cur.next

        cur.next = other

        return startHead

        
                