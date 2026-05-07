# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Linked List Cycle: Determine if a linked list contains a cycle.
        
        TRICK USED:
        - Floyd's Tortoise and Hare Algorithm: Use two pointers moving at different speeds (slow moves 1 step, fast moves 2 steps).
        - If a cycle exists, the fast pointer will eventually "lap" the slow pointer and they will meet at the same node.
        
        WHY IT WORKS:
        - In a linear list, the fast pointer will reach the end (None) quickly.
        - In a cyclic list, the distance between the two pointers increases by 1 in each iteration. Since the relative distance changes,
        - the fast pointer is guaranteed to catch up to the slow pointer within the cycle, regardless of the cycle's length.
        """
        
        # Base case: an empty list cannot have a cycle
        if not head:
            return False
        
        # Initialize pointers: slow starts at head, fast starts one step ahead
        slow = head
        fast = head.next
        
        # Continue while the fast pointer has not reached the end of the list
        while fast and fast.next:
            
            # Advance slow by one node and fast by two nodes
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, a cycle is confirmed
            if slow == fast:
                return True
            
        # Fast pointer reached the end, so no cycle exists
        return False

# COMPLEXITY ANALYSIS:
# T(n) = O(n) - Time Complexity
#   - In the worst case (no cycle), we visit each node once.
#   - In the case of a cycle, the fast pointer catches the slow pointer in linear time relative to the number of nodes.
#
# S(n) = O(1) - Space Complexity
#   - We only use two pointers (slow and fast) regardless of the size of the linked list.