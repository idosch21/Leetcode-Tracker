class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Track the maximum subarray sum found so far
        # Initialize to negative infinity to handle all-negative arrays
        max_sum = float('-inf')
        
        # Track the sum of the subarray ending at the current position
        current_sum = 0
        
        for i in range(len(nums)):
            # Decision: Start a new subarray at current index OR extend the previous subarray
            # - If previous current_sum is negative, it's better to start fresh at nums[i]
            # - Otherwise, extend the subarray by adding nums[i]
            current_sum = max(current_sum + nums[i], nums[i])
            
            # Update the global maximum if the current subarray is larger
            max_sum = max(max_sum, current_sum)
            
        return max_sum

# T(n) = O(n) - single pass through the array
# S(n) = O(1) - only using two variables