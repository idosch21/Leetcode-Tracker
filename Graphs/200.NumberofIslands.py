class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get grid dimensions
        rows = len(grid)
        cols = len(grid[0])
        
        # Four directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Counter for number of islands found
        island_counter = 0
        
        def dfs(row: int, col: int, grid: List[List[str]]):
            # Base case: out of bounds or water ('0')
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return
            
            # Mark current cell as visited by turning it into water
            # This prevents counting the same land cell multiple times
            grid[row][col] = "0"
            
            # Recursively visit all 4 adjacent cells
            # This explores the entire connected land mass
            for dr, dc in directions:
                dfs(row + dr, col + dc, grid)
        
        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Found a new island (land cell)
                if grid[r][c] == "1":
                    island_counter += 1
                    # Run DFS to mark entire island as visited
                    dfs(r, c, grid)
        
        return island_counter

# TRICK: DFS/BFS flood fill. Iterate through grid, when finding '1',
# increment count and run DFS to mark entire connected land as '0'.
# This way we count each island only once.
# T(N) = O(m * n) - visit each cell at most once
# S(N) = O(m * n) - recursion stack in worst case (all land)

