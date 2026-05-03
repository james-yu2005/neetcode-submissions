# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        c1 = list1
        c2 = list2
        while c1 and c2:
            if c1.val <= c2.val:
                dummy.next = c1
                c1 = c1.next
                dummy = dummy.next
            else:
                dummy.next = c2
                c2 = c2.next
                dummy = dummy.next
        while c1:
            dummy.next = c1
            c1 = c1.next
            dummy = dummy.next
        while c2:
            dummy.next = c2
            c2 = c2.next
            dummy = dummy.next
        return head.next