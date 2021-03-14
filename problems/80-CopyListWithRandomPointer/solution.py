"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         def node_copier(node):
#             if node not in nodes:
#                 nodes[node] = Node(node.val)
#             return nodes[node]
        
#         nodes = {None: None}
#         actual = head
        
#         while actual:
#             copy = node_copier(actual)
#             copy.next = node_copier(actual.next)
#             copy.random = node_copier(actual.random)
#             actual = actual.next
#         return nodes[head]

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head: return head
        actual = head
        copy = None
        
        mapping = {}
        
        while actual:
            copy = Node(actual.val)
            mapping[actual] = copy
            actual = actual.next
        
        actual = head
        head = mapping[actual]
        while actual:
            copy = mapping[actual]
            copy.next = mapping.get(actual.next)
            copy.random = mapping.get(actual.random)
            actual = actual.next
        
        return head