class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        size = len(nums)
        
        leftSum = [0] *size
        rightSum = [0] * size
        result = [0] * size
        
        left_temp = nums[0]
        right_temp = nums[size-1]
        
        for i in range(1,size):
            
            leftSum[i] = left_temp
            left_temp += nums[i]
            
        for i in range(size-2,-1,-1):
            rightSum[i] = right_temp
            right_temp += nums[i]
        
        for i in range(size):
            result[i] = abs(rightSum[i]-leftSum[i])
            
        return result