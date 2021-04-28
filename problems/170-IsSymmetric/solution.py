# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if (not root or (not root.left and not root.right)):
            return True
        left = None
        right = None
        lstack = [root.left]
        rstack = [root.right]
        while(lstack and rstack):
            left = lstack.pop()
            right = rstack.pop()
        
            if ((left and not right) or (not left and right)):
                return False
            elif ((left and right) and (left.val != right.val)):
                return False

            if left:
                lstack.append(left.right)
                lstack.append(left.left)

            if right:
                rstack.append(right.left)
                rstack.append(right.right)
        
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p,q):
            if p is not None and q is not None:
                if p.val==q.val:
                    return check(p.left,q.right) and check(p.right,q.left)
                else:
                    return False
            else:
                if p is None and q is None:
                    return True
                else:
                    return False
        return check(root,root)
        
