# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def hasCycle(head):
        
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast:
        fast = fast.next 
        if fast:
            fast = fast.next 
        
        if not fast:
            return False
        
        slow = slow.next
        
        if slow==fast:
            return True