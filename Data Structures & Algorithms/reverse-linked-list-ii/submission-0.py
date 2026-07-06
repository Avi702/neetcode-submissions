# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or right == left:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        before = dummyNode
        for i in range(left-1):
            before = before.next
        segment_end = before.next
        segment = segment_end
        prev = None
        for i in range(right-left+1):
            temp = segment.next
            segment.next = prev
            prev = segment
            segment = temp
        before.next = prev
        segment_end.next = segment
        return dummyNode.next






            

        


            
        

        



            