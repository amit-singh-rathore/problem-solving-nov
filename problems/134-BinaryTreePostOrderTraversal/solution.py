# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     self.visits = []
    #     def postorder(root):
    #         if not root:
    #             return
    #         if root.left:
    #             postorder(root.left)
    #         if root.right:
    #             postorder(root.right)
    #         self.visits.append(root.val)
    #     postorder(root)
    #     return self.visits
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        visits = []
        stack = []
        if not root:
            return visits
        stack.append(root)
        while stack:
            current = stack.pop()
            visits.append(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return visits[::-1]
        