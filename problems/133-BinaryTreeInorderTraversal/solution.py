# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visits = []
        stack = []
        current = root
        while len(stack)>0 or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                visits.append(node.val)
                current = node.right
        return visits
        
#         visits = []
#         self.inorder(root, visits)
#         return visits

#         def inorder(self, node, visits):
#             if not node:
#                 return
#             self.inorder(node.left, visits)
#             visits.append(node.val)
#             self.inorder(node.right, visits)
        
    