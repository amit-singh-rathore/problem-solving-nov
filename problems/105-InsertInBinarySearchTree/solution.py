# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root=TreeNode(val)
            return root
        else:
            return self.insert(val, root)  
    def insert(self, val, curr):
        if curr.val> val:
            if curr.left is None:
                curr.left = TreeNode(val)
            else:
                self.insert(val, curr.left)

        elif curr.val < val:
            if curr.right is None:
                curr.right = TreeNode(val)
            else:
                self.insert(val,curr.right)

        return curr
        