# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def sortedInsert(head, new_node):
            curr = head
            prev = None
            while(new_node.val > curr.val):
                prev = curr
                curr = curr.next
            if prev == None:
                new_node.next = head
                head = new_node
            else:
                prev.next = new_node
                new_node.next = curr
                
            return head
        
        if head == None:
            return head
        
        curr = head
        while curr != None:
            if (curr.next and curr.next.val < curr.val):
                tmp = curr.next
                curr.next = curr.next.next
                head = sortedInsert(head, tmp)
            else:
                curr = curr.next

        return head