# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result = None
        position = 0
        
        def dfs(node):
            
            nonlocal position,result
            
            if not node or result:
                return
            else:
                
                dfs(node.left)
                position += 1
                if position == k:
                    result = node
                    return
                dfs(node.right)
        dfs(root)
        return result.val