# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
   
        les_head = ListNode()
        grt_head = ListNode()
        les_strt = les_head
        grt_strt = grt_head
        while head != None:
            if head.val < x:
                node = ListNode(head.val)
                head = head.next
                les_head.next = node
                les_head = les_head.next
            else:
                node = ListNode(head.val)
                head = head.next
                grt_head.next = node
                grt_head = grt_head.next
        
        les_head.next = grt_strt.next
        return les_strt.next