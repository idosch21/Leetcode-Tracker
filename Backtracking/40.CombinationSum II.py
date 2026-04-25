class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []
        candidates.sort()
        
        def dfs(index,current_sum):
            
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return
            
            for i in range(index, len(candidates)):
                
                if i> index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                
                dfs(i+1,current_sum + candidates[i])
                
                path.pop()
        dfs(0,0)
        return res
                