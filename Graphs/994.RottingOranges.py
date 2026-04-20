import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = collections.deque()
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        
        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] ==2:
                    queue.append((r,c))
        
        if fresh_count == 0:
            return 0
        size_of_queue = len(queue)
        minutes = 0
        
        while queue:
            for _ in range(size_of_queue):
                curr_r, curr_c = queue.popleft()
                for dr,dc in direction:
                    new_r = dr + curr_r
                    new_c = dc +curr_c
                    
                    if 0<= new_r < rows and 0<= new_c < cols:
                        if grid[new_r][new_c] == 1:
                            fresh_count -=1
                            grid[new_r][new_c] = 2
                            queue.append((new_r,new_c))
            size_of_queue = len(queue)
            if queue:
                minutes +=1
        return -1 if fresh_count else minutes
        