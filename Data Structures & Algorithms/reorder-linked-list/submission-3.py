# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        #find middle
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        slow = temp
        #reverse second half
        newhead = None
        while slow:
            temp = slow.next
            slow.next = newhead
            newhead = slow
            slow = temp
        #interleave
        dummy = ListNode(0)
        ans = dummy
        cur = head
        count = 0
        while cur and newhead:
            if count % 2 == 0:
                dummy.next = cur
                cur = cur.next
            else:
                dummy.next = newhead
                newhead = newhead.next
            count += 1
            dummy = dummy.next
        if cur:
            dummy.next = cur
        if newhead:
            dummy.next = newhead
        head = ans.next

        
        