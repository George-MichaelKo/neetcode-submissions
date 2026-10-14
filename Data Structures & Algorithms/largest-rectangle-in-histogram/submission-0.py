class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # two poniter left and rght
        # distance will be difference in width
        stack = []
        largest = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()
                h = heights[j]
                if stack:
                    l = stack[-1]
                else:
                    l = -1
                w = i - l - 1
                area = h*w
                largest = max(largest,area)
            stack.append(i)
        n = len(heights)
        while stack:
            j = stack.pop()
            h = heights[j]
            if stack:
                l = stack[-1]
            else:
                l = -1
            w = n - l - 1
            area = h*w
            largest = max(largest,area)

        return largest 
