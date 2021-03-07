def reverseList(self, head):
    prev, curr = None, head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
    
# def reverseList(self, head):
#     if not head or not head.next:
#         return head
#     rev = self.reverseList(head.next)
#     head.next.next = head 
#     head.next = None
#     return rev

#  def reverseList(self, head):
#     if not head:
#         return head
#     stack = []
#     while head.next != None:
#         stack.append(head) 
#         head = head.next
#     self.head = head
#     while len(stack) != 0:  
#         head.next = stack.pop()  
#         head = head.next
      
#     head.next = None
    
#     return self.head