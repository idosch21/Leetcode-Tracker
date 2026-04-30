class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Result list to store all valid combinations
        res = []
        # Current path being explored
        path = []
        
        def dfs(index, current_sum):
            # Base case 1: Found valid combination that sums to target
            # Add a copy of current path to results
            if current_sum == target:
                res.append(path[:])  # Append copy, not reference
                return
            
            # Base case 2: Sum exceeds target - prune this branch
            if current_sum > target:
                return
            
            # Try each candidate starting from 'index' (allows reuse)
            for i in range(index, len(candidates)):
                # Include current candidate in path
                path.append(candidates[i])
                
                # Recurse with updated sum, same index allows repetitions
                dfs(i, current_sum + candidates[i])
                
                # Backtrack: remove last added candidate
                # This allows trying other combinations
                path.pop()
        
        # Start DFS from index 0 with sum 0
        dfs(0, 0)
        return res

# TRICK: Backtracking with DFS. Try each candidate, recurse, backtrack.
# Key: pass same index i to allow reusing same element (combinations not permutations).
# Prune branches when sum > target.
# T(N) = O(n^(target/min)) - exponential in worst case
# S(N) = O(target/min)
                