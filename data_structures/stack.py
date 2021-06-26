class Stack:
    def __init__(self, stack = []):
        self.stack = stack
        
    def push(self, item):
        self.stack.append(item)
    
    def pop(self, item):
        if len(self.stack) > 0:
            return self.stack.pop(item)
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
    
    def clear(self):
        self.stack.clear()