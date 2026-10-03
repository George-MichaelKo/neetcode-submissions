class Solution:
    def rob(self, nums: List[int]) -> int:
        hashMap = dict()
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in hashMap:
                return hashMap[i]
                
            rob = nums[i] + dfs(i+2)
            skip = dfs(i+1)
            hashMap[i] = max(rob, skip)
            return hashMap[i]
        return dfs(0)   