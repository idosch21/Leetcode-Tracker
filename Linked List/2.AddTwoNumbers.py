# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add Two Numbers: Sum two numbers represented by linked lists in reverse order.
        
        TRICK USED:
        - Dummy Head: Using a placeholder node (dummy) to simplify the construction of the result list, avoiding "if head is None" checks.
        - Carry Propagation: Using a single 'carry' variable to manage values >= 10, mimicking schoolbook addition.
        - Unified While Loop: The condition 'while l1 or l2 or carry' ensures we handle cases where lists have different lengths or an extra digit is created by a final carry.
        
        WHY IT WORKS:
        - Since the digits are stored in reverse order, the first nodes represent the 1s place, the second represent the 10s place, and so on.
        - By traversing both lists simultaneously, we add corresponding digits and carry over any overflow to the next iteration.
        """
        
        # Create a placeholder node to start building the new linked list
        dummy = ListNode()
        # Pointer to keep track of the current tail in the new list
        node = dummy
        # Stores the overflow from the sum of digits (either 0 or 1)
        carry = 0
        
        # Continue as long as there are digits in either list or a carry remains
        while l1 or l2 or carry:
            # Extract values from current nodes, defaulting to 0 if a list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of current digits and the previous carry
            total = val1 + val2 + carry
            
            # Extract the single digit for the new node (e.g., 13 % 10 = 3)
            digit = total % 10
            # Calculate the new carry (e.g., 13 // 10 = 1)
            carry = total // 10
            
            # Create a new node with the calculated digit and link it
            node.next = ListNode(digit)
            # Move the pointer to the newly created node
            node = node.next
            
            # Advance l1 and l2 pointers if they are not yet at the end
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        # Return the list starting from the node after the dummy placeholder
        return dummy.next

# 

# COMPLEXITY ANALYSIS:
# T(n) = O(max(m, n)) - Time Complexity
#   - m and n are the lengths of l1 and l2 respectively.
#   - We iterate through the lists at most max(m, n) times.
#
# S(n) = O(max(m, n)) - Space Complexity
#   - The length of the new list is at most max(m, n) + 1.
#   - Each node in the result list requires constant extra space.