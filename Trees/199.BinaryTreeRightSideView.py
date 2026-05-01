# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Result list to store rightmost values at each level
        res = []
        
        # Handle empty tree edge case
        if not root:
            return []
        
        # Queue for BFS level-order traversal
        queue = collections.deque()
        queue.append(root)
        
        # Process level by level
        while queue:
            # Number of nodes at current level
            size_of_level = len(queue)
            
            # Process all nodes at current level
            for i in range(size_of_level):
                # Get next node from queue
                current_node = queue.popleft()
                
                # If this is the last node at this level, it's the rightmost
                # Add its value to result (right side view)
                if i == size_of_level - 1:
                    res.append(current_node.val)
                
                # Add children to queue for next level
                # Left child first, then right (standard BFS order)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            # Update size for next level
            size_of_level = len(queue)
        
        return res

# TRICK: BFS level-order traversal. Process level by level, capture
# the rightmost node (last in each level). Use queue size to track levels.
# T(N) = O(n)
# S(N) = O(w) where w = max width of tree