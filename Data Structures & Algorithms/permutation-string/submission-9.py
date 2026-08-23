class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0]*26
        window_freq = [0]*26
        l = 0
        k = len(s1)
        for r in range(len(s2)):
            i = ord(s2[r]) - ord('a')
            if r < k:
                j = ord(s1[r]) - ord('a')
                s1_freq[j] += 1
            window_freq[i]+=1
            while (r-l+1) > k:
                window_freq[ord(s2[l]) - ord('a')] -= 1
                l+=1

            if ( r >= (k-1)) and s1_freq == window_freq:
                return True
            
        return False