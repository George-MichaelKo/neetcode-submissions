class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0]*26
        window_freq = [0]*26
        for char in s1:
            idx = ord(char) - ord('a')
            s1_freq[idx] += 1
        l = 0
        k = len(s1)
        for r in range(len(s2)):
            window_freq[ord(s2[r]) - ord('a')]+=1
            while (r-l+1) > k:
                window_freq[ord(s2[l]) - ord('a')] -= 1
                l+=1

            if s1_freq == window_freq:
                return True
            
        return False