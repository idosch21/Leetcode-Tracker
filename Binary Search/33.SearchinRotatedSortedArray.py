class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search in Rotated Sorted Array: Find target in a rotated sorted array
        
        TRICK USED:
        - Modified binary search for rotated arrays where array is sorted in two segments
        - Determine which half (left or right) is sorted by comparing nums[left] vs nums[mid]
        - If left half is sorted (nums[left] <= nums[mid]), check if target is in left range
        - If right half is sorted, check if target is in right range
        - This ensures we always search the correct half while maintaining O(log n) time
        
        WHY IT WORKS:
        - In a rotated sorted array, at least one half will always be sorted
        - By identifying which half is sorted, we can make the same decision as regular binary search
        - We eliminate half the search space each iteration, just like standard binary search
        - The rotation doesn't break the logarithmic elimination property
        """
        
        # Initialize pointers for the search window
        left = 0
        right = len(nums) - 1
        
        # Continue while search window is valid
        while left <= right:
            
            # Calculate mid index
            mid = (left + right) // 2
            
            # Found target at mid
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted (nums[left] to nums[mid] is sorted)
            if nums[left] <= nums[mid]:
                
                # Target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    # Search left half by moving right pointer
                    right = mid - 1
                else:
                    # Search right half by moving left pointer
                    left = mid + 1
            else:
                # Right half is sorted (nums[mid] to nums[right] is sorted)
                
                # Target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    # Search right half by moving left pointer
                    left = mid + 1
                else:
                    # Search left half by moving right pointer
                    right = mid - 1
                    
        # Target not found
        return -1

# COMPLEXITY ANALYSIS:
# T(n) = O(log n) - Time Complexity
#   - Each iteration eliminates half the search space
#   - Same logarithmic time as standard binary search
#   - Constant work per iteration (comparisons and pointer updates)
#
# S(n) = O(1) - Space Complexity
#   - Only constant extra space for left, right, and mid pointers
#   - No additional data structures or recursion