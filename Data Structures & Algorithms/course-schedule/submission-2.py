class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x,y in prerequisites:
            graph[x].append(y)
        completed = set()
        visiting = set()
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
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True



        