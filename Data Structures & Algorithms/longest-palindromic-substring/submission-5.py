class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        longest = 0

        n = len(s)
        for i in range(n):
            l = i
            r = i
            # for odd palindrome length
            while l >=0 and r < n and s[l] == s[r]:
                if (r-l+1) > longest:
                    substring = s[l:r+1]
                    longest = r-l+1
                l -= 1
                r += 1
            #for even palindrome
            l = i
            r = i+1
            while l>=0 and r<n and s[l] == s[r]:
                if (r-l+1) > longest:
                    substring = s[l:r+1]
                    longest = r-l+1
                l -= 1
                r += 1
        return substring
