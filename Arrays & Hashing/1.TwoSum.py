class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map: value -> index
        my_map = {}
        
        for i in range(len(nums)):
            # What number do we need to reach target?
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

# TRICK: Hash map for O(1) lookup. Store each number as we iterate,
# check if its complement already exists. When found, return indices.
# T(N) = O(n)
# S(N) = O(n)