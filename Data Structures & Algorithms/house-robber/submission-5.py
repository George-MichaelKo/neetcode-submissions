class Solution:
    def rob(self, nums: List[int]) -> int:
        largest = float('-inf')
        hashMap = dict()
        n = len(nums)
        def dfs(house):
            if house >= n:
                return 0
            if house in hashMap:
                rob = hashMap[house]
            else:
                rob = dfs(house+2) + nums[house]
                hashMap[house] = rob
            skip = dfs(house + 1)
            return max(rob,skip)

        return dfs(0)
        