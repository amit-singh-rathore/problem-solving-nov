# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = -float("inf")
    def helper(self,node):
        if(node is None):
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)

        sideways= max(node.val, max(left, right)+node.val)
        inorder = max(sideways, left+right+node.val)
        self.res = max(self.res, inorder)
        return sideways
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.res
        