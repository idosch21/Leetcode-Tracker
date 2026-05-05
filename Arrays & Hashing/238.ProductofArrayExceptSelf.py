class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size = len(nums)
        result = [1]*size
        prefix = 1
        
        for i in range(size):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(size-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result 