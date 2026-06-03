class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        
        def dfs(index,current_set):
            
            result.append(current_set.copy())
            
            for i in range(index,len(nums)):
                
                current_set.append(nums[i])
                
                dfs(i+1,current_set)
                
                current_set.pop()
                
        dfs(0,[])
        return result
    