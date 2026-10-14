class Solution:
    def rob(self, nums: List[int]) -> int:
        hashMap = dict()
        n = len(nums)
        def dfs(house):
            if house >= n:
                return 0
            if house in hashMap:
                return hashMap[house]
            rob = dfs(house+2) + nums[house]
            skip = dfs(house + 1)
            hashMap[house] = max(rob,skip)
            return hashMap[house]
        return dfs(0)
        