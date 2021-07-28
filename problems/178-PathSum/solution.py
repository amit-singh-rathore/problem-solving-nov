# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if targetSum - root.val == 0 and not(root.left or root.right):
            return True
        left = self.hasPathSum(root.left, targetSum-root.val)
        right = self.hasPathSum(root.right, targetSum-root.val)
        return left or right

# Optimized 
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, target):
            if not node:
                return False
            is_leaf = False if node.left or node.right else True
            target = target - node.val 
            if is_leaf and target == 0:
                return True
            return dfs(node.left, target) or dfs(node.right, target)

        return dfs(root, targetSum)