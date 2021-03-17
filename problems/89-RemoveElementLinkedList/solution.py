# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
            prev = prev.next
            if curr:
                curr = curr.next
        return dummy.next