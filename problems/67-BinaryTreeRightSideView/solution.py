# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        self.h = -1
        def getright(root,height):
            if root is None:
                return
            if height > self.h:
                ans.append(root.val)
                self.h = height
            getright(root.right, height + 1)
            getright(root.left, height + 1)
        getright(root,0)
        return ans