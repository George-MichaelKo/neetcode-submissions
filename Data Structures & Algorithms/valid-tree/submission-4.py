from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False
            seen.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0,-1):
            return False
        return n == len(seen)



        