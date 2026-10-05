class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Write your solution here
      #hashap 0:1
      # prefix compute
      # store prefix freq in hash map
      # iterate through prefix and find missing number check in dict and addd value to total count
      # return count 

      hashMap = defaultdict(int)
      hashMap[0] += 1
      count = 0
      for i in range(len(nums)):
        if i != 0:
          nums[i] += nums[i-1]
        need = nums[i] - k
        if need in hashMap:
          count += hashMap[need]
        hashMap[nums[i]] += 1
      return count 
          

    

        