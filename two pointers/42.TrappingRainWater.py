class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        maxLeft , maxRight = height[left],height[right]
        counter = 0
        while left < right:
            minHeight = min(maxLeft,maxRight)
            if maxLeft <= maxRight:##we shift left +1
                left+=1
                maxLeft= max(maxLeft,height[left])
                counter+= maxLeft-height[left]
                
                
            else:#maxLeft> maxRight
                right-=1
                maxRight= max(maxRight,height[right])
                counter+= maxRight-height[right]
                
        return counter


