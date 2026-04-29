class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        current_number = nums[0]
        current_counter = 1
        
        for i in range(1,len(nums)):
            if nums[i] == current_number:
                current_counter +=1
            else:
                current_counter -=1
                if current_counter ==0:
                    current_number = nums[i]
                    current_counter =1
        return current_number