class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(houses):
            hashMap = dict()
            n = len(houses)
            def dfs(house):
                if house >= n:
                    return 0
                if house in hashMap:
                    return hashMap[house]
                rob = dfs(house + 2) + houses[house]
                skip = dfs(house + 1)
                hashMap[house] = max(rob, skip)
                return hashMap[house]
            return dfs(0)
               
        return max(helper(nums[:-1]),helper(nums[1:]))