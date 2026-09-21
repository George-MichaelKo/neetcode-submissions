from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()

        components = 0
        def dfs(node, parent):
            if node in visited:
                return 
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
        
        for node in range(n):
            if node in visited:
                continue
            else:
                components += 1
                dfs(node, -1)
        return components
