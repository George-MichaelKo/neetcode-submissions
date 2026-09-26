class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #index 0 or index 1
        # cost of step to i + 1 and i+ 2 = cost[i]
        #len(cost)
        #fibonacci
        top = len(cost)
        costMap = dict()
        def dfs(i):
            if i >= top:
                return 0
            if i in costMap:
                return costMap[i]
            pathCost =  min(dfs(i+1), dfs(i+2)) + cost[i]
            costMap[i] = pathCost
            return pathCost
        return min(dfs(0), dfs(1))
        