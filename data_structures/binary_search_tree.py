class BST:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left:
                return self.left.add(data)
            else:
                self.left = BST(data=data)
                return True
        else:
            if self.right:
                return self.right.add(data)
            else:
                self.right = BST(data=data)
                return True

    def find(self, data):
        if self.data == data:
            return True, self
        elif self.data > data:
            if self.left:
                return self.left.find(data)
            else:
                return False, None
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False, None

    def remove(self, data, parent=None, subtree=None):
        if self.data == data:
            if self.left is None and self.right is None:
                if parent is not None and subtree is not None:
                    setattr(parent, subtree, None)
                else:
                    self.data = None
            elif self.left and self.right:
                val = self.__get_next_highest(data)
                self.data = val
            elif self.left and not self.right:
                parent.left = self.left
            else:
                parent.right = self.right
        elif self.data > data:
            if self.left:
                self.left.remove(data, self, "left")
            else:
                return False
        else:
            if self.right:
                self.right.remove(data, self, "right")
            else:
                return False

    def __get_next_highest(self, data):
        is_found, node = self.find(data)

        parent = node
        if is_found:
            node = node.right
            if not node.left:
                parent.right = None
                return node.data

            while node.left is not None:
                parent = node
                node = node.left
            val_to_return = node.data
            parent.left = None
        return val_to_return

    def get_size(self):
        if self.left and self.right:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1

    def preorder(self):
        if self:
            print(self.data, end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data, end=' ')