# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque([root])
        result = []

        level = 0
        
        while queue:
            temp = deque()
            len_level = len(queue)
            for _ in range(len_level):
                current = queue.popleft()
                
                if level %2 == 0:
                    temp.append(current.val)
                else:
                    temp.appendleft(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(list(temp))
            level+=1
        return result
            