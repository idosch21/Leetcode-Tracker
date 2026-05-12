# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        
        scout = dummy
        
        while scout and scout.next:
            if scout.next.val == val:
                scout.next = scout.next.next
            else:
                scout= scout.next
        return dummy.next