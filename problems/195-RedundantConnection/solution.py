class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        count = n
        for e in edges:         
            node1, node2 = e

            while parent[node1] != node1:
                node1 = parent[node1]

            while parent[node2] != node2:
                node2 = parent[node2]

            if node1 == node2:
                return e
            
            parent[node2] = node1