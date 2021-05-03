# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, val):
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.helper(root.left, val)
        else:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.helper(root.right, val)
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        l = len(preorder)
        if l == 0:
            return None
        root = TreeNode(preorder[0])
        idx = 1
        queue = [root]
        
        
        while idx < l:
            self.helper(root, preorder[idx])
            idx += 1
        return root
