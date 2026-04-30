class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Result list to store all permutations
        result = []
        
        def dfs(current_path, used_set):
            # Base case: path length equals nums length - complete permutation
            # Add a copy of current path to results
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
            
            # Try each unused number
            for num in nums:
                # Skip if number is already in current path
                if num in used_set:
                    continue
                
                # Add number to current path
                current_path.append(num)
                # Mark number as used
                used_set.add(num)
                
                # Recurse to build the rest of permutation
                dfs(current_path, used_set)
                
                # Backtrack: remove number from path
                current_path.pop()
                # Unmark number as used
                used_set.remove(num)
        
        # Start DFS with empty path and empty used set
        dfs([], set())
        return result

# TRICK: Backtracking with used set. Try each unused number, recurse,
# backtrack. Unlike combinations, order matters (permutations not combinations).
# Use set to track which numbers are currently in path.
# T(N) = O(n * n!) - generate all n! permutations
# S(N) = O(n)