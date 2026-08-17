from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0; r = 0
        n = len(s)
        output = 0
        while r < n:
            freq[s[r]]+=1

            top = max(freq.values()) 
            while ((r-l+1) - top) > k:
                freq[s[l]]-=1
                l+=1
                top = max(freq.values()) 
            output=max(output, r-l+1)
            r+=1
            
        return output
            
        