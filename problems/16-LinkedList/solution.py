class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    
    #initialization code
    def __init__(self):
        self.head =  None
    
    # implementing iter so that we can loop over the linked list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    
    def prepend(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None: 
            self.head = new_node
            return
        
        last = self.head 
        while (last.next): 
            last = last.next
        
        last.next =  new_node
    
    def insert_before(self, target_node, new_node):
        if not self.head:
            raise Exception("List is empty")
        
        if self.head.data == target_node:
            return self.prepend(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        
        raise Exception("Target node '%s' not found" % target_node)
    
    def insert_after(self, target_node, new_node):
        if not self.head:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Target Node '%s' not found" % target_node)
    
    def delete_node(self, target_node):
        if not self.head:
            raise Exception("List is empty")
            
        if self.head.data == target_node:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Target Node '%s' not found" % target_node_data)
    
    def display(self): 
        temp = self.head 
        nodes = []
        while temp is not None: 
            nodes.append(temp.data)
            temp = temp.next
        nodes.append("Null")
        print( " -> ".join(nodes))
        
        
linked_list = LinkedList() 
linked_list.display()
linked_list.prepend("b") 
linked_list.display()
linked_list.prepend("a")
linked_list.display()

linked_list.append("e"); 
linked_list.display()
linked_list.insert_after("b", Node("c")) 
linked_list.display()

linked_list.insert_before("e",Node("d"))
linked_list.display()
linked_list.insert_before("e",Node("ee"))
linked_list.display()
linked_list.delete_node("ee")
linked_list.display()
  