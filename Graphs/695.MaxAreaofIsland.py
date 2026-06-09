class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        max_area = 0

        def dfs(row,col):
            
            if row<0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            
            area = 1
            grid[row][col] == 0
            
            for dr, dc in directions:
                new_r = dr + row
                new_c = dc + col
                area += dfs(new_r,new_c)
                
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area,dfs(r,c))
                    
        return max_area