class Node:  
    def __init__(self, value):  
        self.left = None
        self.right = None
        self.value = value 

def print_ancestors(root, target):
    if not root: 
        return False 
      
    if root.value == target: 
        return True 
  
    if (print_ancestors(root.left, target) or print_ancestors(root.right, target)):
        print(root.value)
        return True
    return False
