class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        neeed = 0
        have = 0 
        ans = float('-inf')
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0)+1

            have = max(freq.values())
            window_size = r-l+1
            need = window_size - have

            while need > k:
                freq[s[l]] -= 1
                l+=1
                have = max(freq.values())
                window_size = r-l+1
                need = window_size - have
            ans = max(ans, r-l+1)
        return ans

        