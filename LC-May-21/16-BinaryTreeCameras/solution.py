# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            l=0
            r=0
            if (node.left is None and node.right is None):
                return -1
            if node.left:
                l = dfs(node.left)
            if node.right:
                r = dfs(node.right)
            if(l == -1 or r == -1):
                self.count += 1
                return 1
            if(l == 0 and r == 0):
                return -1
            if(l == 1 or r == 1):
                return 0
        self.count=0
        cams = dfs(root)
        if(cams == -1):
            self.count += 1
        return self.count

