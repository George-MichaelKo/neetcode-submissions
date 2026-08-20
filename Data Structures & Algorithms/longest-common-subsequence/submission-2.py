from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        @cache
        def dfs(t1,t2):
            if t1 >= m or t2 >= n:
                return 0
            if text1[t1] == text2[t2]:
                return 1 + dfs(t1+1, t2+1)
            dfs(t1,t2+1)
            dfs(t1+1,t2)

            return max(dfs(t1,t2+1), dfs(t1+1,t2))
        return dfs(0,0)
