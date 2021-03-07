# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return head

    current = dummy = ListNode(-1, head)
    while current and current.next:
        dup = current.next
        while dup.next and dup.val == dup.next.val:
            dup = dup.next
        if current.next!= dup:
            current.next = dup.next
        else:
            current = current.next
    return dummy.next