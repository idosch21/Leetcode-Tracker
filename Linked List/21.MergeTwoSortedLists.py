# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge Two Sorted Lists: Merge two sorted linked lists into one sorted list
        
        TRICK USED:
        - Use a dummy node as the starting point to avoid special handling of the head
        - Use a tail pointer to track the end of the merged list as we build it
        - Compare the current heads of both lists and append the smaller value
        - Move the corresponding list pointer forward and update tail
        - Finally, append any remaining nodes from the non-empty list
        
        WHY IT WORKS:
        - Both input lists are already sorted, so we can greedily pick the smaller head
        - By always taking the smaller value, we maintain sorted order in the result
        - The dummy node simplifies the logic by providing a consistent starting point
        - This approach processes each node exactly once, achieving optimal efficiency
        """
        
        # Create dummy node to simplify head handling
        dummy = ListNode()
        # Tail pointer tracks the end of our merged list
        tail = dummy
        
        # Handle edge cases where one list is empty
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Merge while both lists have nodes
        while list1 and list2:
            
            # Compare current values and append the smaller one
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Move tail to the newly added node
            tail = tail.next
            
        # Append any remaining nodes from the non-empty list
        tail.next = list1 if list1 else list2
        
        # Return the merged list (skip dummy node)
        return dummy.next
    
    """ this is the recursive way T(n) = O(n+m), S(n) = O(n+m)
        if not list1:
            return list2
        if not list2:
            return list1

        if(list1.val <= list2.val):
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
"""

# COMPLEXITY ANALYSIS:
# T(n) = O(n + m) - Time Complexity
#   - We process each node from both lists exactly once
#   - n and m are the lengths of list1 and list2 respectively
#   - Each comparison and pointer update is O(1)
#
# S(n) = O(1) - Space Complexity
#   - Iterative approach uses only constant extra space
#   - Dummy node and tail pointer don't scale with input size
#   - No recursion stack or additional data structures