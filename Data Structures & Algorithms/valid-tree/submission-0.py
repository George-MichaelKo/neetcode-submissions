from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #adjcency list 
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        def dfs(node, parent):
            
            if node in visited:
                return False
            
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
            visiting.remove(node)
            completed.add(node)
        
        if not dfs(0, -1):
            return False
                
        return n == len(visited)


        