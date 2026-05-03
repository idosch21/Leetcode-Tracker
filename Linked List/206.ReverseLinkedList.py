# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse Linked List: Reverse a singly linked list iteratively
        
        TRICK USED:
        - Use three pointers: prev (tracks previous node), current (current node being processed),
          and nxt (temporary storage for next node to avoid losing the reference)
        - Iterate through the list, reversing the direction of each node's next pointer
        - Move all pointers forward: prev = current, current = nxt
        
        WHY IT WORKS:
        - By reversing the next pointers one by one, we change the direction of the entire chain
        - The prev pointer becomes the new head of the reversed list
        - Each node gets its next pointer updated to point to the previous node instead of next
        - This iterative approach avoids recursion and maintains O(1) space complexity
        """
        
        # Handle empty list case
        if not head:
            return None
        
        # Initialize pointers: prev tracks the reversed portion, current is the node to process
        prev = None
        current = head
        
        # Iterate through the entire list
        while current:
            # Save the next node before we overwrite current.next
            nxt = current.next
            
            # Reverse the current node's pointer to point to the previous node
            current.next = prev
            
            # Move prev forward to current (now part of reversed list)
            prev = current
            
            # Move current forward to the next node to process
            current = nxt
            
        # prev now points to the head of the reversed list
        return prev

# COMPLEXITY ANALYSIS:
# T(n) = O(n) - Time Complexity
#   - We visit each node exactly once in the while loop
#   - Each iteration performs constant-time operations (pointer assignments)
#   - Linear time proportional to the number of nodes
#
# S(n) = O(1) - Space Complexity
#   - Only using three pointer variables (prev, current, nxt) regardless of list size
#   - No additional data structures or recursion stack