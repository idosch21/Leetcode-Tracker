class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointers: start from both ends
        start = 0
        end = len(heights) - 1
        # Track maximum area found
        max_area = 0
        
        # Move pointers towards each other
        while start < end:
            # Height is limited by shorter line
            min_height = min(heights[start], heights[end])
            # Area = height * width
            current_area = min_height * (end - start)
            
            # Move the pointer with smaller height
            # Why? Shorter line limits area, might find taller line ahead
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            
            # Update maximum area
            max_area = max(max_area, current_area)
        
        return max_area

# TRICK: Two pointers from ends. Calculate area, move pointer with
# shorter height inward. Shorter line bounds the area, so moving it
# might find a taller one. Greedy approach works.
# T(N) = O(n)
# S(N) = O(1)