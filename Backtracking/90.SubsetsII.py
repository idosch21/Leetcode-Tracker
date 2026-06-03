class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        
        def dfs(index,current_set):
            
            result.append(current_set.copy())
            
            for i in range(index,len(nums)):
                
                if i > index and nums[i] == nums[i-1]:
                    continue
                
                current_set.append(nums[i])
                
                dfs(i+1,current_set)
                
                current_set.pop()
                
        dfs(0,[])
        return result