from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #have a dfs for connecting and chcking and building graph checking if destination not in visited
        # iterate through edges and buld graph
        visited = set()
        visited.add(edges[0][0])
        def dfs(node, dest, visited):
            if node == dest:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei,dest,visited):
                        return True
            return False
        graph = defaultdict(list)
        for x,y in edges:
        # if i can connect edges without cyclic build graph
            if dfs(x,y,set()):
                return [x,y]
            graph[x].append(y)
            graph[y].append(x)

        