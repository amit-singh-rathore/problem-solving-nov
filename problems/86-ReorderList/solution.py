# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        if len(stack)<3:
            return head
        
        middle = len(stack)//2
        stack[middle].next = None
        
        cur = head
        for i in range(-1, -middle-1, -1): 
            nxt = cur.next
            if nxt == stack[i]:
                break
            stack[i].next = nxt
            cur.next = stack[i]
            cur = nxt
            

        return head