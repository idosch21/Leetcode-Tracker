# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #the idea is to find the middle of the list
        #reverse the second half of the list
        #check if the first half and the reversed second half are equal
        #true else false
        
        slow = head
        fast = head
        
        #finding the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            
        #slow reached the half point
        prev = None
        current = slow
        
        #creating the reversed list
        while current:
            nxt = current.next
            current.next = prev
            prev = current
        
        #now prev is the reversed list
        left , right = head,prev
        while right:
            if left.val == right.val:
                left = left.next
                right=right.next
                
            else:
                return False
        return True
            
        