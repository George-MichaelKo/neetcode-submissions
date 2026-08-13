class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        seq = set()
        for num in nums:
            if (num - 1) not in nums:
                curr_c = 1    
                while (num+1) in nums:
                    curr_c += 1
                    num = num+1
                count = max(count, curr_c) 
            else:
                continue        
        return count
