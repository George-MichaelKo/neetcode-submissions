
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #0 -> 1 

        #0 -> 1  <- 0
        #1->0

        visiting = set()
        completed = set()
        preMap = defaultdict(list)
        for course, pre in prerequisites:
            preMap[course].append(pre) #adjcency list 
        #1:[1], 0:[1]

        def dfs(node):
            if node in visiting:
                return False
            visiting.add(node)
            for course in preMap[node]:
                if course in completed:
                    continue
                if not dfs(course):
                    return False
            visiting.remove(node)
            completed.add(node)
            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return False
        return len(completed) == numCourses



        
