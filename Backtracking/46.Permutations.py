class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def dfs(current_path,used_set):
            
            if len(current_path)==len(nums):
                result.append(list(current_path))
                return
            for num in nums:
                if num in used_set:
                    continue
                current_path.append(num)
                used_set.add(num)
                dfs(current_path,used_set)
                
                current_path.pop()
                used_set.remove(num)
        dfs([],set())
        return result