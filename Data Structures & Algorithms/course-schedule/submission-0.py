from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
     # numCourses = 2, prerequisites = [[0,1]]
     #1 -> 0 

     #1->0 ->1

    #create prerequites Adjacency list - Graph 
    #path set
    #dfs for checkinh if i can take a course
        visiting = set()
        completed = set()
        preMap = defaultdict(list)
        for course, preq in prerequisites:
            preMap[course].append(preq)
        
        def dfs(course):
            if course in visiting:
                return False
            if course in completed:
                return True
            visiting.add(course)
            for preq in preMap[course]:
                if not dfs(preq):
                    return False
            visiting.remove(course)
            completed.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True



