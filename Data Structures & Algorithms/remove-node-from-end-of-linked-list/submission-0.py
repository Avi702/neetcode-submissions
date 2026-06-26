# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        countR = 1
        R = head
        while R and R.next:
            R = R.next
            countR +=1
        target = countR - n
        dummyNode = ListNode(0,head)
        L = dummyNode
        countL = 1
        for i in range(target):
            L = L.next
        L.next = L.next.next
        return dummyNode.next

            
        
            

