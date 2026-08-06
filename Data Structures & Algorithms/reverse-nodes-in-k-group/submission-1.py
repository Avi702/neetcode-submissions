# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupprev = dummy
        while True:
            length = 0
            newhead = groupprev.next
            while newhead and length < k:
                length += 1
                newhead = newhead.next
            if length < k:
                return dummy.next
            groupnext = newhead
            prev = groupnext
            cur = groupprev.next
            length = 0
            while cur != groupnext and length < k:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = groupprev.next
            groupprev.next = prev
            groupprev = temp

            
