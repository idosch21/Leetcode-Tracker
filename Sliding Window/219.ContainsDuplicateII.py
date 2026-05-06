class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        left = 0
        my_set = set()
        
        for right in range(len(nums)):
            
            if nums[right] in my_set:
                return True
            my_set.add(nums[right])
            
            if right-left+1 > k:
                my_set.remove(nums[left])
                left+=1
                
        return False