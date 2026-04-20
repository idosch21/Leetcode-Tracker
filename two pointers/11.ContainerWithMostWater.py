class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights) - 1
        max_area = 0

        while start<end:
            min_height = min(heights[start],heights[end])
            current_area = min_height * (end-start)
            if heights[start] < heights[end]:
                start+=1
            else:
                end -=1
            max_area = max(max_area,current_area)

        return max_area