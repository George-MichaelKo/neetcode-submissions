from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        components = 0
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node, parent):
            if node in seen:
                return
            seen.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
        for node in range(n):
            if node not in seen:
                components += 1
                dfs(node, -1)
        return components
