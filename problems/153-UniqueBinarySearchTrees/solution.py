class Solution:
    def numTrees(self, n: int) -> int:
        tabulation = [1, 1]
        for nodes in range(2, n+1):
            tabulation.append(0)
            for node in range(nodes):
                tabulation[nodes] += tabulation[node] * tabulation[nodes-node-1]
        return tabulation[n]
        