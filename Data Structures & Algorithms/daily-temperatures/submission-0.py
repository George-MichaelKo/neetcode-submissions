class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0]*n
        stack = []
        for i in range(n):

            while stack and stack[-1][0] < temperatures[i]:
                w = stack.pop()
                output[w[1]] = i - w[1]
            stack.append((temperatures[i],i))
        return output
            
        