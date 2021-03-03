from heapq import heappush, heappop

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeKLists(lists):
    i_head = head = ListNode(0)
    
    min_heap = []
    for row_num, node in enumerate(lists):
        if node:
            heappush(min_heap, (node.val, row_num, node))
    
    while min_heap:
        val, row_num, node = heappop(min_heap)
        head.next = node
        head = head.next
        if node.next:
            heappush(min_heap, (node.next.val, row_num, node.next))
    return i_head.next
    
