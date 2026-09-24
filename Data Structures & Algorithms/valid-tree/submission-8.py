from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(course, parent):
            if course in visited:
                return False
            visited.add(course)
            for nei in graph[course]:
                if nei == parent:
                    continue
                if not dfs(nei,course):
                    return False
            return True
        #check cycle
        if not dfs(0,-1):
            return False
        
        #check connected
        return len(visited) == n
                


        