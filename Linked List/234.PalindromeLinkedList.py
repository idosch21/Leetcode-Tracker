# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle using slow/fast pointers
        # - slow moves 1 step, fast moves 2 steps
        # - when fast reaches end, slow is at middle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half starting from 'slow'
        prev = None
        current = slow
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        # Step 3: Compare first half with reversed second half
        # 'prev' is head of reversed second half
        left, right = head, prev
        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        
        return True

# TRICK: Find middle with slow/fast, reverse second half, compare.
# T(N) = O(n)
# S(N) = O(1)
            
        