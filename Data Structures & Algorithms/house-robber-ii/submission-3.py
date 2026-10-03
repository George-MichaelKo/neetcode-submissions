class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(array):
            hashMap = dict()
            def dfs(i):
                if i >= len(array):
                    return 0
                if i in hashMap:
                    return hashMap[i]
                rob = array[i] + dfs(i+2)
                skip = dfs(i+1)
                hashMap[i] = (max(rob, skip))
                return hashMap[i]
            return dfs(0)
        n = len(nums)
        # if len(nums) == 1:
        #     return nums[0]
        return max(nums[0],helper(nums[0:n-1]),helper(nums[1:])) 
        