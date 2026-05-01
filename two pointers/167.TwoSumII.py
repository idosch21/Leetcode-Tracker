class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers: start from both ends of sorted array
        start = 0
        end = len(numbers) - 1
        
        # Move pointers towards each other
        while start < end:
            # Calculate current sum
            current_sum = numbers[start] + numbers[end]
            
            if current_sum == target:
                # Found valid pair - return 1-based indices
                return [start + 1, end + 1]
            
            elif current_sum > target:
                # Sum too large - decrease end pointer to reduce sum
                end -= 1
            else:
                # Sum too small - increase start pointer to increase sum
                start += 1

# TRICK: Two pointers on sorted array. Since array is sorted,
# if sum > target, move end left; if sum < target, move start right.
# Works because there's exactly one valid solution.
# T(N) = O(n)
# S(N) = O(1)
        