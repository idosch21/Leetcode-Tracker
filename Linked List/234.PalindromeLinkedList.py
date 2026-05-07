# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Palindrome Linked List: Check if a linked list reads the same forward and backward.
        
        TRICK USED:
        - Slow and Fast Pointers: Use the two-pointer technique to find the middle of the list in a single pass.
        - In-Place Reversal: Reverse the second half of the linked list starting from the middle node to allow for a direct value comparison.
        - Symmetry Check: Compare values from the start of the original list and the start of the reversed second half simultaneously.
        
        WHY IT WORKS:
        - A palindrome is symmetrical. By reversing the second half of the list, the "tail" becomes a second "head."
        - If the list is a palindrome, the first half and the reversed second half will be identical in sequence.
        - Reversing in-place allows the check to be performed with constant extra space, which is more efficient than copying the list to an array.
        """
        
        
        # Step 1: Find the middle of the linked list
        # 'slow' moves one step while 'fast' moves two; when 'fast' hits the end, 'slow' is at the middle.
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list starting from the 'slow' pointer
        # This converts the second half into a reversed segment for easy comparison.
        prev = None
        current = slow
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        # Step 3: Compare the first half and the reversed second half
        # 'prev' is now the head of the reversed second half.
        left, right = head, prev
        while right:
            # Compare values; if any pair doesn't match, it's not a palindrome.
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        
        # All corresponding values matched.
        return True

# COMPLEXITY ANALYSIS:
# T(n) = O(n) - Time Complexity
#   - Finding the middle takes O(n/2) time.
#   - Reversing the second half takes O(n/2) time.
#   - Comparing the two halves takes O(n/2) time.
#   - The overall performance remains linear.
#
# S(n) = O(1) - Space Complexity
#   - The reversal is done in-place by changing node pointers.
#   - No auxiliary data structures (like arrays or stacks) are used, only a few pointer variables.