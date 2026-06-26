# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        L,R = head, head
        M = head
        cur_head = head
        while R and R.next:
            prev1 = M
            M = M.next
            R = R.next.next
        prev1.next = None
        prev = None
        while M:
            temp = M.next
            M.next = prev
            prev = M
            M = temp
        M = prev
        while L and M:
            tempL = L.next
            tempM = M.next
            L.next = M
            if tempL:
                M.next = tempL
            L = tempL
            M = tempM
        return

        
        
        

        
        