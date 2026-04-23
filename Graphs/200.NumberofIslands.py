class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        island_counter = 0
        
        def dfs(row:int , col: int , grid: List[List[str]]):

            if row<0 or row >= rows or col<0 or col>=cols or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                for dr, dc in directions:
                    dfs(dr+row,dc+col , grid)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_counter +=1
                    dfs(r,c,grid)
        return island_counter

