class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        s_frq = {}
        t_frq = {}
        small = float('inf')
        sub=""
        have = 0
        need = len(t)
        for char in t:
            t_frq[char]= t_frq.get(char, 0)+1
        l = 0
        for r in range(len(s)):
            s_frq[s[r]]= s_frq.get(s[r], 0)+1
            if s[r] in t and s_frq[s[r]] <= t_frq[s[r]]:
                have+=1
            while have >= need :
                
                if (r-l+1) < small:
                    small = (r-l+1)
                    sub = s[l:r+1]

                if s[l] in t and s_frq[s[l]] == t_frq[s[l]] :
                    have-=1

                s_frq[s[l]]-=1
                l+=1
        return sub
        