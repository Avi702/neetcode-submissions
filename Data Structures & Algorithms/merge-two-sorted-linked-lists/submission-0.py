# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        ans = dummyNode
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            temp1 = list1
            temp2 = list2
            if list1.val <= list2.val:
                dummyNode.next = temp1
                list1 = list1.next
            else:
                dummyNode.next = temp2
                list2 = list2.next
            dummyNode = dummyNode.next
        if list1:
            dummyNode.next = list1
        elif list2:
            dummyNode.next = list2
        return ans.next

                

