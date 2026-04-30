import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Queue for BFS - stores coordinates of rotten oranges
        queue = collections.deque()
        
        # Four directions: right, left, down, up
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Count of fresh oranges remaining
        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # First pass: count fresh oranges and add rotten ones to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    # Add all rotten oranges as starting points
                    queue.append((r, c))
        
        # If no fresh oranges, return 0 (already done)
        if fresh_count == 0:
            return 0
        
        # Track time in minutes
        minutes = 0
        
        # BFS: process level by level (each level = 1 minute)
        while queue:
            # Process all oranges that rotted at the same time
            size_of_queue = len(queue)
            
            for _ in range(size_of_queue):
                curr_r, curr_c = queue.popleft()
                
                # Try all 4 adjacent cells
                for dr, dc in direction:
                    new_r = curr_r + dr
                    new_c = curr_c + dc
                    
                    # Check if within bounds
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        # If fresh orange, it becomes rotten
                        if grid[new_r][new_c] == 1:
                            fresh_count -= 1
                            grid[new_r][new_c] = 2
                            queue.append((new_r, new_c))
            
            # After processing current level, increment minutes
            # Only if there are more oranges to process
            if queue:
                minutes += 1
        
        # If fresh_count > 0, some oranges couldn't be reached
        return -1 if fresh_count else minutes

# TRICK: Multi-source BFS. Start with all rotten oranges in queue,
# process level by level. Each level = 1 minute. Use grid modification
# to mark newly rotten oranges. Check if any fresh remain at end.
# T(N) = O(m * n) - visit each cell at most once
# S(N) = O(m * n) - queue can hold all rotten oranges
        