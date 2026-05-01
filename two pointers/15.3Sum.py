class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Strategy: Fix one number, use two-pointer for remaining two
        # Convert to 2-sum problem: find a+b = -c
        
        # Sort to enable two-pointer and duplicate skipping
        nums.sort()
        
        # Result list to store valid triplets
        ans = []
        
        # Fix first number (a)
        for i in range(len(nums)):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two-pointer for remaining two numbers
            # Target sum = -nums[i] (we need a + b = -c)
            start = i + 1
            end = len(nums) - 1
            
            # Two-pointer search
            while start < end:
                total = nums[start] + nums[end] + nums[i]
                
                if total > 0:
                    # Sum too large - decrease end pointer
                    end -= 1
                elif total < 0:
                    # Sum too small - increase start pointer
                    start += 1
                else:
                    # Found valid triplet
                    ans.append([nums[start], nums[end], nums[i]])
                    
                    # Move start past duplicates
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        
        return ans

# TRICK: Sort + fix one number + two-pointer for remaining two.
# Skip duplicates at each level to avoid duplicate triplets.
# T(N) = O(n²)
# S(N) = O(n) for sorting or O(1) extra

            
