# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)

        size_of_level = len(queue)
        while queue:
            
            for i in range(size_of_level):
                current_node = queue.popleft()
                if i == size_of_level-1:
                    res.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            size_of_level = len(queue)
        return res