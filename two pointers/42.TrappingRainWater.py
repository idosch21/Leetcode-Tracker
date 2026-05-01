class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers from both ends
        left = 0
        right = len(height) - 1
        
        # Track maximum height seen from left and right
        maxLeft = height[left]
        maxRight = height[right]
        
        # Water trapped accumulator
        counter = 0
        
        # Process until pointers meet
        while left < right:
            # Water level is determined by shorter boundary
            minHeight = min(maxLeft, maxRight)
            
            # Move pointer with smaller max height
            if maxLeft <= maxRight:
                # Left side has smaller boundary - move left pointer
                left += 1
                # Update maxLeft if current height is higher
                maxLeft = max(maxLeft, height[left])
                # Water at this position = boundary height - actual height
                counter += maxLeft - height[left]
            else:
                # Right side has smaller boundary - move right pointer
                right -= 1
                # Update maxRight if current height is higher
                maxRight = max(maxRight, height[right])
                # Water at this position = boundary height - actual height
                counter += maxRight - height[right]
        
        return counter

# TRICK: Two pointers + tracking max from each side. Water at each
# position = min(maxLeft, maxRight) - height[i]. Move pointer with
# smaller max, update max, calculate water. O(n) single pass.
# T(N) = O(n)
# S(N) = O(1)


