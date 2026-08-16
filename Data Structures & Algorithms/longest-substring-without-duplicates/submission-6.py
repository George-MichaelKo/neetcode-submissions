class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        window = set()
        max_len = 0

        while r < n:
            while l < r and s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            max_len = max(max_len, r-l+1)
            r+=1
        return max_len
        