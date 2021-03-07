# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque([{'node' : root , 'height' : 1}])

        
        while queue:
            queueItem = queue.popleft()
            
            node = queueItem['node'] 
            height = queueItem['height'] 
            
            if not node.left and not node.right:     
                return height  

            if node.left: 
                queue.append({'node' : node.left , 'height' : height + 1})

            if node.right:   
                queue.append({'node' : node.right , 'height' : height + 1}) 