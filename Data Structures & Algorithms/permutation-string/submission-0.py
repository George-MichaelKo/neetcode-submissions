class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char,0)+1
        s2_freq = {}
        l = 0
        k = len(s1)
        for r in range(len(s2)):
            s2_freq[s2[r]] = s2_freq.get(s2[r],0)+1
            while (r-l+1) > k:
                s2_freq[s2[l]] -= 1

                if s2_freq[s2[l]] == 0:
                    del s2_freq[s2[l]]
                l+=1
            if s1_freq == s2_freq:
                return True
            
        return False