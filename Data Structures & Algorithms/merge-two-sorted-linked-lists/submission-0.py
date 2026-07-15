# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            head_address = list1
            head = list1
            b = list2
        else:
            head_address = list2
            head = list2
            b = list1
        while head.next is not None:
            if b.val < head.next.val:
                c = head.next
                head.next = b
                b = c
            else:
                head = head.next
            
        head.next = b
        return head_address