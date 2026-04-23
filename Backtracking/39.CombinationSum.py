class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []
        
        def dfs(index,current_sum):
            
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return
            
            for i in range(index, len(candidates)):
                
                path.append(candidates[i])
                
                dfs(i,current_sum + candidates[i])
                
                path.pop()
        dfs(0,0)
        return res
                