import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Rotting Oranges: Find the minimum time required for all fresh oranges to rot.
        
        TRICK USED:
        - Multi-Source Breadth-First Search (BFS): Instead of starting BFS from a single point, we initialize the queue with all cells containing rotten oranges (grid value 2).
        - Level-Order Traversal: We process the queue level by level, where each full level represents exactly one minute of time passing.
        - Fresh Orange Counter: Tracking the number of fresh oranges at the start allows for an O(1) check at the end to see if any remained untouched.
        
        WHY IT WORKS:
        - BFS is designed to find the shortest path in an unweighted graph. In this grid, the "distance" is time. 
        - Starting with all rotten oranges simultaneously ensures we find the earliest possible moment each fresh orange is reached by the rot.
        - By decrementing the fresh_count as we go, we avoid a second full-grid scan at the end.
        """
        
        # Queue for BFS to store coordinates of rotten oranges
        queue = collections.deque()
        
        # Four directions: right, left, down, up
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Determine grid dimensions and initialize fresh orange counter
        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # First pass: Count fresh oranges and collect all initial sources of rot
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    # Add all rotten oranges to the queue as starting points
                    queue.append((r, c))
        
        # Early exit: if no fresh oranges exist, no time is needed
        if fresh_count == 0:
            return 0
        
        # Track elapsed time in minutes
        minutes = 0
        
        # Multi-source BFS: process oranges level by level
        while queue:
            # size_of_queue captures all oranges that rotted in the same minute
            size_of_queue = len(queue)
            
            for _ in range(size_of_queue):
                curr_r, curr_c = queue.popleft()
                
                # Check all four neighbors for fresh oranges
                for dr, dc in direction:
                    new_r = curr_r + dr
                    new_c = curr_c + dc
                    
                    # Ensure neighbor is within grid bounds
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        # If a fresh orange is found, it becomes rotten
                        if grid[new_r][new_c] == 1:
                            fresh_count -= 1
                            grid[new_r][new_c] = 2
                            queue.append((new_r, new_c))
            
            # Increment time only if new oranges were added to the queue for the next minute
            if queue:
                minutes += 1
        
        # If any fresh oranges remain, it means they were unreachable by the rot
        return -1 if fresh_count else minutes

# COMPLEXITY ANALYSIS:
# T(n) = O(M * N) - Time Complexity
#   - M is rows, N is columns.
#   - We iterate over the grid once initially to count and find rot.
#   - Each cell is added to and removed from the queue at most once.
#
# S(n) = O(M * N) - Space Complexity
#   - In the worst case (e.g., all oranges are rotten), the queue will hold M * N elements.
#   - We modify the grid in-place, so no extra grid storage is required.