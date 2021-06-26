class Node:
    def __init__(self, data, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def __str__(self):
        return f"Node({self.data})"

class SinglyLinkedList:
    def __init__(self, root: Node = None):
        self.root = root
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
        new_root_node = Node(val, next_node=self.root)
        self.root = new_root_node
        self.size += 1

    def find(self, val):
        curr_node = self.root
        while curr_node is not None:
            if curr_node.data == val:
                return val
            else:
                curr_node = curr_node.next_node
        return False

    def remove(self, val):
        curr_node = self.root
        prev_node = None

        while curr_node is not None:
            if curr_node.data == val:
                if prev_node is None:
                    self.root = curr_node.next_node
                else:
                    prev_node.next_node = curr_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = curr_node
                curr_node = curr_node.next_node
        return False