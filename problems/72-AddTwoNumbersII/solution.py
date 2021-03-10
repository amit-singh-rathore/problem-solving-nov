# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_stack, l2_stack = [], []
        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next
        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next
        dum = ListNode(0)
        cfwd = 0
        while l1_stack or l2_stack or cfwd:
            dgt1 = l1_stack.pop() if l1_stack else 0
            dgt2 = l2_stack.pop() if l2_stack else 0
            cur = dgt1 + dgt2 + cfwd
            cfwd, cur = divmod(cur, 10)
            cur_node = ListNode(cur)
            cur_node.next = dum.next
            dum.next = cur_node
        return dum.next
        