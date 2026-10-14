from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        visiting = set()
        completed = set()
        order = []
        def dfs(course):
            if course in completed:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            completed.add(course)
            order.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
    
        return order 

        