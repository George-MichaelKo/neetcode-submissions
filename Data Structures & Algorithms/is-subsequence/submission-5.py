from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0    
        while i < len(s):
            for j in range(j, len(t)):
                if s[i] == t[j]:
                    i+=1
                    j = j+1
                    break
            else:
                return False
        return True

        