class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        for num in nums:
            if (num-1) not in nums:
                curr_count = 1
                while (num+1) in nums:
                    curr_count+=1
                    num+=1
                count = max(count, curr_count)
            else:
                continue
        return count