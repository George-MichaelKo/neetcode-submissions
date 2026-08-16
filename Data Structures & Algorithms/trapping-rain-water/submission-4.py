class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = r_max = 0
        l_max_arr = [0] * n
        r_max_arr = [0] * n
        i = 0; r = n-1
        while i < n:
            l_max_arr[i]=l_max
            r_max_arr[r]=r_max
            l_max = max(l_max, height[i])
            r_max = max(r_max, height[r])
            r-=1
            i+=1
        
        total_water = 0
        for j in range(n):
            total = min(l_max_arr[j],r_max_arr[j]) - height[j]
            total_water += max(0,total)
        return total_water
          
        