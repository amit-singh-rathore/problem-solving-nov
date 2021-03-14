# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None, head)
        hstart = lagger = dummy
        for _ in range(n + 1):
            hstart = hstart.next
        while hstart:
            hstart = hstart.next
            lagger = lagger.next
        lagger.next = lagger.next.next
        return dummy.next        