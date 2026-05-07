class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find Minimum in Rotated Sorted Array: Locate the pivot point in a sorted array that has been rotated.
        
        TRICK USED:
        - Binary search comparing the middle element with the rightmost element of the current window.
        - If nums[middle] > nums[right], it proves the "inflection point" (the minimum) is in the right half.
        - If nums[middle] <= nums[right], the right half is correctly sorted, so the minimum must be at middle or to its left.
        
        WHY IT WORKS:
        - In a rotated sorted array, there is exactly one point where the value drops.
        - By comparing mid to right, we can determine which segment is "disrupted" by the rotation.
        - Unlike standard binary search, we don't need a target; we use the array's own properties to shrink the search space.
        """
        
        # Initialize pointers for the binary search window
        left = 0
        right = len(nums) - 1
        
        # Continue until the window collapses to a single element
        while left < right:
            
            # Calculate the midpoint index
            middle = (left + right) // 2
            
            # Check if the middle element is greater than the right boundary
            if nums[middle] > nums[right]:
                # Minimum must be in the right half, middle is definitely not the minimum
                left = middle + 1
            else:
                # Minimum is either at middle or in the left half
                right = middle
        
        # Left and right converge on the smallest element
        return nums[right]

# COMPLEXITY ANALYSIS:
# T(n) = O(log n) - Time Complexity
#   - Each step reduces the search range by half, maintaining logarithmic performance.
#   - Constant time logic (comparisons) per iteration.
#
# S(n) = O(1) - Space Complexity
#   - Only a fixed number of integer pointers (left, right, middle) are used.
#   - No extra memory relative to the input size.