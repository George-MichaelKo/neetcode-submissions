class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                minI = stack.pop()
                h = heights[minI]
                w = i - stack[-1]-1 if stack else i
                area = h*w
                largest = max(largest,area)
            stack.append(i)
        n = len(heights)
        while stack:
            j = stack.pop()
            w = n - stack[-1] - 1 if stack else n
            largest = max(largest, heights[j] * w )
        return largest  
