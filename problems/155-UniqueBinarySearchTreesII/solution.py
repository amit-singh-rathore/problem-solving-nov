# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(beg, end):
            if (end < beg): return [None]
            if (end == beg): return [TreeNode(beg)]
            result = []
            for i in range(beg - 1, end):
                leftResult = helper(beg, i)
                rightResult = helper(i + 2, end)            
                for left in leftResult:
                    for right in rightResult:
                        result.append(TreeNode(i + 1, left, right))
            return result
        return helper(1, n)