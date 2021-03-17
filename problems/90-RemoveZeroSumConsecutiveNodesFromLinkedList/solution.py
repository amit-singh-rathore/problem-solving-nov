# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        
        while True:
            head, s = dummy.next, 0
            map_sum = {0: dummy}
            while head:
                s += head.val
                if s in map_sum:
                    map_sum[s].next = head.next
                    break
                map_sum[s] = head
                head = head.next
            else:
                break
        return dummy.next
        