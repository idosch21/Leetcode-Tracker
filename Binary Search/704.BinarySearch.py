class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search: Find target in a sorted array
        
        TRICK USED:
        - Use two pointers (left and right) to maintain a search window
        - Calculate mid = (left + right) // 2 to divide the search space in half
        - Based on comparison of nums[mid] vs target, eliminate half the remaining elements
        
        WHY IT WORKS:
        - Array is sorted, so we can make decisions to skip half the elements each iteration
        - By comparing target with mid element, we determine which half to search next
        - This logarithmic elimination of search space reduces time complexity from O(n) to O(log n)
        """
        
        # Initialize pointers to track the search window
        left = 0
        right = len(nums) - 1
        
        # Continue searching while the window is valid (left <= right)
        while left <= right:
            
            # Calculate mid index (using integer division to avoid overflow)
            mid = (left + right) // 2
            
            # Found the target at mid position
            if nums[mid] == target:
                return mid
            
            # Target is larger than mid, so search the right half
            elif nums[mid] < target:
                left = mid + 1
            
            # Target is smaller than mid, so search the left half
            else:
                right = mid - 1
                
        # Target not found in the array
        return -1

# COMPLEXITY ANALYSIS:
# T(n) = O(log n) - Time Complexity
#   - We eliminate half the search space in each iteration
#   - Maximum iterations = log2(n) where n is array length
#   - Each iteration does constant work (comparison, pointer update)
#
# S(n) = O(1) - Space Complexity
#   - Only using a constant amount of extra space (left, right, mid pointers)
#   - No additional data structures or recursion stack
                