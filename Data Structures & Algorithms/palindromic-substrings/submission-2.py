class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_palindromes = 0
        
        # Helper function to expand around a center and count palindromes
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            # Expand outwards as long as it's a valid palindrome
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            # Case 1: Odd-length palindromes (centered at a single character s[i])
            total_palindromes += expand_around_center(i, i)
            
            # Case 2: Even-length palindromes (centered between s[i] and s[i+1])
            total_palindromes += expand_around_center(i, i + 1)
            
        return total_palindromes 
        