# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.freq_map = {}
        self.populateArray(root)
        return self.get_mode()
        
        
    def populateArray(self, root):
        if root == None:
            return 
        self.populateArray(root.left)
        self.freq_map[root.val] = self.freq_map.get(root.val, 0)+1
        self.populateArray(root.right)
        root.left = root.right = None
        
    def get_mode(self):
        res = sorted(self.freq_map.items(), key=lambda item: item[1], reverse=True)
        
        out=[res[0][0]]
        for r in range(1,len(res)):
            if res[0][1]==res[r][1]:
                out.append(res[r][0])
            else:
                break
        return out
        
        
                
    
    