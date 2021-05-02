class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = { i: [] for i in range(n) }
        
        for n1, n2  in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        res, visited = 0, set()
        
        for node in graph:
            if node not in visited:
                res += 1
                self.dfs(node, graph, visited)
                
        return res
    
    def dfs(self, node, graph, visited):
        if node in visited:
            return
        
        visited.add(node)
        
        for nei in graph[node]:
            self.dfs(nei, graph, visited)
