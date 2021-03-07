# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def averageOfLevels(root):
    queue = deque([root])
    res = []
    while(queue):
        same_level_values = []
        for i in range(len(queue)):
            out = queue.popleft()
            same_level_values.append(out.val)
            if out.left:
                queue.append(out.left)
            if out.right:
                queue.append(out.right)
        res.append(sum(same_level_values)/len(same_level_values))
    return res 