# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = 1
        left = head
        while n<k:
            left = left.next
            n += 1
        lnode = left
        
        right = head
        while left.next:
            right = right.next
            left = left.next
                
        lnode.val, right.val = right.val, lnode.val
        return head