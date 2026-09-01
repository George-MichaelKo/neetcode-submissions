class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        top = -1
        n = len(nums) 
        for r in range(n):
            total += nums[r]
            if  total < 0 :
                total = 0
                continue
            top = max(top, total) 
        return top
                  