# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        cur = head
        idx = 0
        res, stack = [], []
        while cur:
            while stack and cur.val > stack[-1][1]:
                i, v = stack.pop()
                res[i] = cur.val
            stack.append((idx, cur.val))
            idx += 1
            res.append(0)
            cur = cur.next
        return res
        