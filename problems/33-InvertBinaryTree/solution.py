def invertTree(root):
    if root:
        left, right = root.left, root.right
        root.left, root.right = right, left
        self.invertTree(root.left)
        self.invertTree(root.right)
    return root

# def invertTree(root):
#     if not root:
#         return root
    
#     queue = deque()
    
#     result = []
#     queue.append(root)
    
#     while queue:
#         node = queue.popleft()
#         node.left , node.right = node.right, node.left
#         if node.left != None:
#             queue.append(node.left)
#         if node.right != None:
#             queue.append(node.right)
#     return root
            
        