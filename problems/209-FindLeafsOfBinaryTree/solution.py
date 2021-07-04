# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        while root.left or root.right:
            temp = []
            bfs = [root]
            while bfs:
                n_bfs = []
                for node in bfs:
                    if node.left:
                        if not node.left.left and not node.left.right:
                            temp.append(node.left.val)
                            node.left = None
                        else:
                            n_bfs.append(node.left)
                    if node.right:
                        if not node.right.left and not node.right.right:
                            temp.append(node.right.val)
                            node.right = None
                        else:
                            n_bfs.append(node.right)
                bfs = n_bfs
            res.append(temp)
        res.append([root.val])
        return res