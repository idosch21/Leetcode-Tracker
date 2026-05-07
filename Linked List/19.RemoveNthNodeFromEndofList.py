# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove Nth Node From End of List: Remove the node that is n positions from the tail.
        
        TRICK USED:
        - Two-Pointer (Fast & Slow) Gap: We create a "delay" between two pointers. By moving the 'fast' pointer n steps ahead of the 'slow' pointer, we establish a fixed window.
        - Dummy Node: We use a dummy node pointing to the head to handle edge cases, such as removing the very first node of the list.
        
        WHY IT WORKS:
        - When the 'fast' pointer reaches the end of the list (None), the 'slow' pointer, which started n steps behind,
        - will be positioned exactly at the node preceding the one we want to remove.
        - This allows us to reassign the next pointer of the 'slow' node to skip the target node, effectively deleting it in a single pass.
        """
        
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0, head)
        
        # Initialize both pointers at the start of the list
        slow = dummy.next
        fast = dummy.next
        
        # Advance the 'fast' pointer by n + 1 steps to create the necessary gap
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers forward simultaneously until 'fast' reaches the end
        while fast and slow:
            fast = fast.next
            slow = slow.next
        
        # If 'slow' is positioned before the target, skip the nth node from the end
        if slow.next:
            slow.next = slow.next.next
        
        # Return the head of the modified list (skipping dummy)
        return dummy.next

# COMPLEXITY ANALYSIS:
# T(n) = O(L) - Time Complexity
#   - L is the length of the linked list. 
#   - We traverse the list exactly once with the fast pointer.
#
# S(n) = O(1) - Space Complexity
#   - We only use a constant amount of extra space for the dummy node and the two pointers.