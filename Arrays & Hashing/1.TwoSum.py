class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Hash map to store: value -> index
        # Key: the number value, Value: its index in the array
        my_map = {}
        
        for i in range(len(nums)):
            # Calculate what number we need to pair with nums[i] to reach target
            complement = target - nums[i]
            
            # Check if the complement already exists in our hash map
            # If yes, we've found our pair!
            if complement in my_map:
                # We found a pair such that complement + nums[i] == target
                # Return the indices of both numbers
                return [my_map[complement], i]
            
            # If complement not found, add current number to map
            # This allows us to check against it in future iterations
            my_map[nums[i]] = i
        
        # No valid pair found
        return False

# T(n) = O(n) - single pass through the array
# S(n) = O(n) - hash map stores up to n elements