# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #DFS solution with recursion
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        stack = [root]
        preorder = []
        node_path_count = {}
        while stack:
            node = stack.pop()
            preorder.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        diameter = 0
        while preorder:
            node = preorder.pop()
            left = node_path_count.get(node.left, 0)
            right = node_path_count.get(node.right, 0)
            diameter = max(diameter, left + right)
            node_path_count[node] = max(left, right) + 1
        
        return diameter

# Iterative solution using Pre Order Traversal
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res=0
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if not root:
            return 0
        l_path=self.helper(root.left)
        r_path=self.helper(root.right)
        self.res=max(self.res, l_path+r_path)
        return max(l_path, r_path) +1