# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        right_head, right_end = head, head
        
        while right_end and right_end.next:
            left_end = right_head
            right_end = right_end.next.next
            right_head = right_head.next
            
        left_end.next = None
        
        left = self.sortList(head)
        right = self.sortList(right_head)
        
        return self.merge(left, right)
    
    
    def merge(self, left, right):
        
        dummy = ListNode()
        curr = dummy
        
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left 
        else: 
            curr.next = right
        
        return dummy.next