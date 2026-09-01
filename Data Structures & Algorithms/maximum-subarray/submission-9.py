class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        top = nums[0]
        n = len(nums) 
        for r in range(n):
            total += nums[r]
            top = max(top, total) 
            if  total < 0 :
                total = 0    
            
        return top
                  