# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sorted_arry = []
        self.populateArray(root)
        return self.create_balanced_tree(0, len(self.sorted_arry) - 1)
        
        
    def populateArray(self, root):
        if root == None:
            return 
        
        self.populateArray(root.left)
        self.sorted_arry.append(root)
        self.populateArray(root.right)
        root.left = root.right = None

        
    def create_balanced_tree(self, start, end):
        if start > end:
            return None
        
        if start == end:
            return self.sorted_arry[start]

        mid = (start + end )//2
        curr = self.sorted_arry[mid]
        curr.left = self.create_balanced_tree(start, mid - 1)
        curr.right = self.create_balanced_tree(mid + 1, end)

        return curr