class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Maximum Subarray: Find the contiguous subarray with the largest sum.
        
        TRICK USED:
        - Kadane's Algorithm: A greedy/dynamic programming approach that makes a local decision at each index.
        - At each step, we decide whether to "extend" the existing subarray or "restart" a new one starting at the current element.
        - This effectively discards any prefix subarray that has a negative sum, as it would only decrease the potential of future subarrays.
        
        WHY IT WORKS:
        - A subarray with a negative sum is a "liability." If we add a negative prefix to any number, the result will always be smaller than the number itself.
        - By calculating current_sum = max(current_sum + nums[i], nums[i]), we ensure we are always moving forward with the best possible "head start."
        """
        
        # Initialize global maximum to negative infinity to handle arrays consisting only of negative numbers
        max_sum = float('-inf')
        
        # current_sum represents the maximum subarray sum ending at the current index
        current_sum = 0
        
        for i in range(len(nums)):
            # Core Logic: If adding the current element to the previous sum is worse than 
            # just starting over with the current element, we restart the subarray.
            current_sum = max(current_sum + nums[i], nums[i])
            
            # Update the global max if the new local subarray is the largest we've seen
            max_sum = max(max_sum, current_sum)
            
        return max_sum

# COMPLEXITY ANALYSIS:
# T(n) = O(n) - Time Complexity
#   - We perform a single linear pass through the array.
#   - Each iteration involves constant-time arithmetic and comparison operations.
#
# S(n) = O(1) - Space Complexity
#   - We only maintain two variables (max_sum and current_sum) throughout the execution.
#   - No extra data structures are used.