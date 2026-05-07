class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Number of Islands: Count the number of distinct connected components of '1's in a 2D binary grid.
        
        TRICK USED:
        - DFS Flood Fill (Sinking Islands): When a '1' is encountered, it represents a new island. We increment the counter and immediately use DFS to traverse and "sink" (change '1' to '0') all connected land cells.
        - In-place Modification: By modifying the grid directly, we avoid the need for an auxiliary 'visited' data structure.
        
        WHY IT WORKS:
        - Each cell is visited at most a constant number of times. 
        - The nested loops ensure we check every cell, while the DFS ensures that once an island is counted, it is completely removed from future consideration.
        - This effectively partitions the grid into discrete connected components.
        """
        
        # Determine the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Define the relative coordinates for moving down, up, right, and left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Counter to track the total number of islands discovered
        island_counter = 0
        
        def dfs(row: int, col: int, grid: List[List[str]]):
            # Base case: if out of bounds or the cell is water ('0'), stop recursion
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return
            
            # Sink the island: mark the current land cell as visited by changing it to '0'
            grid[row][col] = "0"
            
            # Recursively explore all four neighbors to sink the entire connected landmass
            for dr, dc in directions:
                dfs(row + dr, col + dc, grid)
        
        # Scan the entire grid cell by cell
        for r in range(rows):
            for c in range(cols):
                # If we find a '1', it's the start of a new, uncounted island
                if grid[r][c] == "1":
                    island_counter += 1
                    # Trigger DFS to sink all land belonging to this specific island
                    dfs(r, c, grid)
        
        return island_counter

# COMPLEXITY ANALYSIS:
# T(n) = O(M * N) - Time Complexity
#   - M is the number of rows, N is the number of columns.
#   - We iterate over every cell in the grid once. 
#   - Each land cell is visited by DFS exactly once before being turned to water.
#
# S(n) = O(M * N) - Space Complexity
#   - In the worst case (e.g., a grid filled entirely with land), the recursion stack 
#     can grow to the total number of cells in the grid.