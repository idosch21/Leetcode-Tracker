class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Result list to store all valid combinations
        res = []
        # Current path being explored
        path = []
        
        # Sort candidates to enable duplicate detection
        candidates.sort()
        
        def dfs(index, current_sum):
            # Base case 1: Found valid combination that sums to target
            # Add a copy of current path to results
            if current_sum == target:
                res.append(path[:])  # Append copy, not reference
                return
            
            # Base case 2: Sum exceeds target - prune this branch
            if current_sum > target:
                return
            
            # Try each candidate starting from 'index'
            for i in range(index, len(candidates)):
                # Skip duplicates: if current is same as previous AND
                # previous was not used in this level, skip to avoid duplicates
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include current candidate in path
                path.append(candidates[i])
                
                # Recurse with next index (i+1) - each element can only be used once
                dfs(i + 1, current_sum + candidates[i])
                
                # Backtrack: remove last added candidate
                path.pop()
        
        # Start DFS from index 0 with sum 0
        dfs(0, 0)
        return res

# TRICK: Backtracking with DFS + duplicate skipping. Sort array first,
# then skip duplicates at same level (i > index check). Use i+1 instead
# of i to prevent reusing same element (each number can be used once).
# T(N) = O(n * 2^n) - exponential
# S(N) = O(n)
                