# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        answer = []
        
        while queue:
            temp = []
            level = [ el.val for el in queue if el]
            if level:
                answer.append(level)

            for el in queue:
                if el:
                    if el.left != None:
                        temp.append(el.left)
                    if el.right != None:
                        temp.append(el.right)
            queue = temp
    
        return answer
            
        
        