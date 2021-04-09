# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     self.visits = []
    #     def preorder(root):
    #         if not root:
    #             return
    #         self.visits.append(root.val)
    #         if root.left:
    #             preorder(root.left)
    #         if root.right:
    #             preorder(root.right)
    #     preorder(root)
    #     return self.visits
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        visits = []
        while root or stack:
            while root:
                stack.append(root)
                visits.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        return visits