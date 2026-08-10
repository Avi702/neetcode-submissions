# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummy = dummyNode
        carry = False
        while l1 and l2:
            if carry:
                total = l1.val + l2.val + 1
                carry = False
            else:
                total = l1.val + l2.val
            if total >= 10:
                carry = True
            dummy.next = ListNode(total%10)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            if carry:
                total = l1.val + 1
                carry = False
            else:
                total = l1.val
            if total >= 10:
                carry = True
            dummy.next = ListNode(total%10)
            dummy = dummy.next
            l1 = l1.next
        while l2:
            if carry:
                total = l2.val + 1
                carry = False
            else:
                total = l2.val
            if total >= 10:
                carry = True
            dummy.next = ListNode(total%10)
            dummy = dummy.next
            l2 = l2.next
        if carry:                   
            dummy.next = ListNode(1)
        return dummyNode.next