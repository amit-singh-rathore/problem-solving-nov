# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or (not head.next):
            return head
        
        prev=head
        curr=head.next
        nhead=curr
		
        while curr:            
            nxt = curr.next 
            curr.next = prev  
            if not nxt:
                prev.next = None
                curr=nxt
            else:
                if nxt.next:
                    prev.next = nxt.next
                else:
                    prev.next = nxt
                prev=nxt;
                curr = nxt.next
        head=nhead
        return head      
    
        