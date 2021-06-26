class Node:
    def __init__(self, data, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def __str__(self):
        return f"Node({self.data})"

class DoublyLinkedList:
    def __init__(self, root: Node = None):
        self.root = root
        self.last = root
        self.size = 0

    def __str__(self):
        if self.root is None:
            return "None"

        curr_node = self.root
        linked_list_repr = ""
        while curr_node is not None:
            linked_list_repr += f"->{str(curr_node)}"
            curr_node = curr_node.next_node
        return linked_list_repr

    def add(self, val):
        if self.size == 0:
            self.root = self.last = Node(val)
        else:
            new_node = Node(val, next_node=self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, val):
        curr_node = self.root
        while curr_node is not None:
            if curr_node.data == val:
                return val
            else:
                curr_node = curr_node.next_node
        return None

    def remove(self, val):
        curr_node = self.root

        while curr_node.next_node is not None:
            if curr_node.data == val:
                if curr_node.prev_node and curr_node.next_node:
                    curr_node.prev_node.next_node = curr_node.next_node
                    curr_node.next_node.prev_node = curr_node.prev_node
                elif curr_node == self.root:
                    self.root = curr_node.next_node
                    self.root.prev_node = self.root
                else:
                    curr_node.prev_node.next_node = None
                    self.last = curr_node.prev_node

                self.size -= 1
                return True
            else:
                curr_node = curr_node.next_node

        return False