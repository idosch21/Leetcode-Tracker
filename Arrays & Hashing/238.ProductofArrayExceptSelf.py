class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array and set initial prefix multiplier
        size = len(nums)
        result = [1] * size
        prefix = 1
        
        # Left-to-right pass: store the product of all elements before i
        for i in range(size):
            result[i] = prefix
            prefix *= nums[i]
        
        # Right-to-left pass: multiply the prefix product by the postfix product
        postfix = 1
        for i in range(size - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result 

# TRICK: Two-pass approach (prefix and postfix) to compute products without using division.
# T(N) = O(n)
# S(N) = O(1) (excluding output array)