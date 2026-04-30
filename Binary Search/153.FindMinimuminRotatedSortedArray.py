class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search boundaries
        left = 0
        right = len(nums) - 1
        
        # Continue until left meets right
        while left < right:
            # Calculate middle index
            middle = (left + right) // 2
            
            # If middle element > right element, minimum is in right half
            # (rotated portion must be to the right of middle)
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                # If middle element <= right element, minimum is in left half
                # (including middle itself)
                right = middle
        
        # Left == right points to minimum element
        return nums[right]

# TRICK: Binary search with comparison against right element.
# If nums[middle] > nums[right], min is in right half (left = middle + 1).
# Otherwise, min is in left half (right = middle).
# T(N) = O(log n)
# S(N) = O(1)