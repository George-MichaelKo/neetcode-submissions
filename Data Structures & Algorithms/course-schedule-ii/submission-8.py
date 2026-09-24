from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #[102, 101] [course, pre]
        # directed graph 

        # graph[0] = []
        # graph[1] = [0]

        # 1->0

        # completed = courses
        # visiting = 0,1 
        #completed = 0, 1
        #path = list()
        # if completed : completed 
        # if course in visiting == cycle return 

        preMap = defaultdict(list)
        for x, y in prerequisites:
            preMap[x].append(y)
        visiting = set()
        completed = set()
        
        def dfs(course):
            if course in completed:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            completed.add(course)
            path.append(course)
            return True
        path = []
        for course in range(numCourses):
            if not dfs(course):
                return []   
        return path
        
        
        