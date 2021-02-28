# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def detectCycle(self, head: ListNode) -> ListNode:
    slow = head
    fast = head
    
    while fast:
        fast = fast.next 
        if fast:
            fast = fast.next 
        if not fast:
            return None
        
        slow = slow.next
        
        if slow==fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow