# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def wrapper(node):
            
            if not node:
                return (True,0)
            
            left_balanced , left_h = wrapper(node.left)
            right_balanced,right_h = wrapper(node.right)
            
            if left_balanced and right_balanced and abs(left_h-right_h)<=1:
                return (True,1+max(left_h,right_h))
            else:
                return (False,-1)
        
        return wrapper(root)[0]