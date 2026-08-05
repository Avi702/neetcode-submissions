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
            ref = groupprev.next
            while ref and length < k:
                ref = ref.next
                length += 1
            if length < k:
                return dummy.next
            groupnext = ref
            prev = groupnext
            cur = groupprev.next
            length = 0
            while cur != groupnext and length < k:
                length += 1
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = groupprev.next
            groupprev.next = prev
            groupprev = temp
            


            
            

