# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or (not head.next) or k ==0:
            return head
            
        node = head
        l = 0
        while node:
            node = node.next
            l +=1
        
        k =  k%l
        if k == 0:
            return head
        
        fast = head
        slow = head
        while(k>0):
            fast = fast.next
            k -= 1
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        curr_head = slow.next
        slow.next = None
        fast.next = head
        
        return curr_head
            
        
        
            
        