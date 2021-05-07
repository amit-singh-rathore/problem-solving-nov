# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        left=self.binaryTreePaths(root.left)
        right=self.binaryTreePaths(root.right)
        res = left + right
        if res:
            return [str(root.val)+"->"+i for i in res]
        return [str(root.val)]