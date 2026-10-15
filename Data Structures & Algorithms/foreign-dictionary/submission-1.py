class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}

        for i in range(len(words)-1):
            minL = min(len(words[i]), len(words[i+1]))
            if words[i][:minL] == words[i+1][:minL] and len(words[i]) > len(words[i+1]) :
              return ""
            for c in range(minL):
              if words[i][c] != words[i+1][c]:
                adj[words[i][c]].add(words[i+1][c])
                break
        visiting = set()
        completed = set()
        res = []
        def dfs(char):
          if char in completed:
            return True
          if char in visiting:
            return False
          visiting.add(char)
          for nei in adj[char]:
            if not dfs(nei):
              return False
          visiting.remove(char)
          completed.add(char)
          res.append(char)
          return True

        for c in adj:
          if not dfs(c):
            return ""
        return "".join(res[::-1])
          
        
    
          
          
      
        