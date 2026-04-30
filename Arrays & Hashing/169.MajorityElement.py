class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Start with first element as candidate
        current_number = nums[0]
        current_counter = 1
        
        # Iterate through remaining elements
        for i in range(1, len(nums)):
            if nums[i] == current_number:
                # Same as candidate - increment count
                current_counter += 1
            else:
                # Different from candidate - decrement count
                current_counter -= 1
                if current_counter == 0:
                    # Count reached 0 - new candidate
                    current_number = nums[i]
                    current_counter = 1
        
        return current_number

# TRICK: Boyer-Moore Voting Algorithm. Count +1 for candidate,
# -1 for others. When count = 0, switch candidate. Majority appears > n/2 times.
# T(N) = O(n)
# S(N) = O(1)